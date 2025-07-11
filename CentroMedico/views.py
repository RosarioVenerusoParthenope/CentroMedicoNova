from django.db.models import Prefetch         # Usato in: visualizza_prenotazione, visite_non_completate – per ottimizzare query sui related
import sqlite3                                # Usato in: login_auth_raw_unsafe – per eseguire query raw non sicure (a scopo didattico)
from django.contrib import messages           # Usato in: login_auth, registrazione, aggiungi_prenotazione, gestione_prestazioni – per messaggi utente
from django.contrib.auth.hashers import *     # Usato in: registrazione, login_auth – per make_password e check_password
from django.db.models import Prefetch         # (duplicato, già presente sopra)
from django.db.models import Sum, Max         # Usato in: visualizza_fatture – per somma costi esami e data referti
from django.http import HttpResponse          # Usato in: download_fattura_pdf – per restituire il PDF
from django.shortcuts import redirect         # Usato in: login_auth, logout, registrazione, aggiungi_prenotazione, gestione_prestazioni – per redirect
from django.shortcuts import render           # Usato in quasi tutte le view – per rendere template HTML
from django.template.loader import get_template  # Usato in: download_fattura_pdf – per caricare template del PDF
from xhtml2pdf import pisa                    # Usato in: download_fattura_pdf – per generare PDF da HTML
from datetime import datetime                 # Usato in: gestione_prestazioni – per validare date
from django.db.models import Count            # Usato in: aggiungi_prenotazione – per contare prestazioni assegnate ai medici/tecnici

# Form personalizzati
from CentroMedico.form import *               # Usato in: registrazione, aggiungi_prenotazione – per i form HTML del paziente

# Modelli del progetto
from CentroMedico.models import *             # Usato in quasi tutte le view – per accedere ai modelli: Paziente, Prenotazione, Prestazione, ecc.

# Utility Django
from django.shortcuts import render, get_object_or_404  # Usato in: render in molte view, get_object_or_404 è importato ma **non utilizzato**





def home(request):

    return render(request, 'home.html')


def visite_non_completate(request):
    visite = VisitaMedica.objects.filter(
        prestazioni__referto__isnull=True
    ).distinct().select_related(
        "id_prenotazione", "id_prenotazione__id_paziente"
    ).prefetch_related(
        "prestazioni__id_esame",
        "prestazioni__personale__id_personale"
    )

    return render(request, "visite_non_completate.html", {
        "visite_da_completare": visite
    })



def login(request):

    return render(request, 'login.html')


#Per authRAW
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
#creazione cursore
cursor = conn.cursor()

#  test per sql injection

def login_auth_raw_unsafe(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        query = f"""
            SELECT id_paziente,nome FROM CentroMedico_paziente 
            WHERE email = '{email}' AND password = '{password}'
        """
        cursor.execute(query)
        row = cursor.fetchone()
        print(row[0])

        if row:

            return render(request, 'dashboard_paziente.html', {'nome': row[1]})
        else:
            return render(request, 'login.html', {'error': 'Credenziali non valide'})


def login_auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Verifica se esiste un paziente con quell'email
        if Paziente.objects.filter(email=email).exists():
            user = Paziente.objects.get(email=email)
            if check_password(password, user.password):
                print(user.password)
                request.session['user_type'] = 'paziente'
                request.session['user_id'] = user.id_paziente
                return render(request, 'dashboard_paziente.html', {'nome': user.nome})

        # Verifica se esiste un membro del personale con quell'email
        if Personale.objects.filter(email=email).exists():
            user = Personale.objects.get(email=email)
            if check_password(password, user.password):
                if user.ruolo.lower() == 'medico':  # controllo sul ruolo (case insensitive)
                    request.session['user_type'] = 'personale'
                    request.session['user_id'] = user.id_personale
                    return render(request, 'dashboard_personale.html', {'nome': user.nome})
                else:
                    messages.error(request, "Accesso consentito solo ai medici.")
            else:
                messages.error(request, "Password errata.")
        else:
            messages.error(request, "Utente non trovato.")

        return render(request, 'login.html', {'error': 'Credenziali non valide'})

def logout(request):
    try:
        del request.session["user_id"]
        del request.session["user_type"]
    except KeyError:
        pass
    return render(request, 'home.html', {'logout': "Utente Disconnesso"})

#FUNZIONI PAZIENTE

def registrazione(request):

    if request.method == 'POST':
        form = RegistrazioneForm(request.POST)
        if form.is_valid():
            paziente = Paziente(
                #form.cleaned_data → un dizionario con i valori del form, già puliti e tipizzati.
                nome=form.cleaned_data['nome'],
                cognome=form.cleaned_data['cognome'],
                data_nascita=form.cleaned_data['data_nascita'],
                codice_fiscale=form.cleaned_data['codice_fiscale'],
                sesso=form.cleaned_data['sesso'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),

            )
            # con make password Algoritmo sicuro (PBKDF2),Salt,Iterazioni (più lento = più sicuro)
            paziente.save()

            messages.success(request, "Registrazione effettuata con successo!")

            return redirect('home')  # cambia con l'URL giusto
    else:
        form = RegistrazioneForm()

    return render(request, 'registration.html', {'form': form})
def aggiungi_prenotazione(request):
    if request.method == 'POST':
        form = PrenotazioneForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data_prenotazione']
            sede = form.cleaned_data['sede']
            esami_selezionati = form.cleaned_data['esami']
            user_id = request.session.get("user_id")
            paziente = Paziente.objects.get(id_paziente=user_id)

            # Crea la prenotazione
            prenotazione = Prenotazione.objects.create(
                data_prenotazione=data,
                id_paziente=paziente
            )

            # Crea la visita medica
            visita = VisitaMedica.objects.create(
                id_prenotazione=prenotazione,
                data_visita=None,
                sede=sede
            )
            #esami selezionati li prende dalle checkbox, più elementi cecco => crea array di esami
            for esame in esami_selezionati:
                # Collega l’esame alla prenotazione
                ListaEsami.objects.create(
                    id_prenotazione=prenotazione,
                    id_esame=esame
                )

                # Crea la prestazione collegata alla visita e all'esame
                prestazione = Prestazione.objects.create(
                    id_esame=esame,
                    codice_visita=visita
                )

                # Assegna il medico in base alla specializzazione e carico
                specializzazione = esame.categoria
                medici = Personale.objects.filter(
                    specializzazione=specializzazione,
                    ruolo__icontains='medico'
                ).annotate(
                    num_prestazioni=Count('prestazioni')
                ).order_by('num_prestazioni')  # medico meno occupato per primo

                if medici.exists():
                    medico_scelto = medici.first()
                    PersonalePrestazione.objects.create(
                        id_prestazione=prestazione,
                        id_personale=medico_scelto
                    )

                # Se è diagnostica per immagini, assegna anche un tecnico
                if esame.categoria == "Radiologia":
                    tecnici = Personale.objects.filter(
                        specializzazione=specializzazione,
                        ruolo__icontains='tecnico'
                    ).annotate(
                        num_prestazioni=Count('prestazioni')
                    ).order_by('num_prestazioni')

                    if tecnici.exists():
                        tecnico_scelto = tecnici.first()
                        PersonalePrestazione.objects.create(
                            id_prestazione=prestazione,
                            id_personale=tecnico_scelto
                        )

            messages.success(request, "Prenotazione effettuata con successo!")
            return redirect('dashboard_paziente')
        else:
            messages.error(request, "Errore nel form. Controlla i campi.")
    else:
        form = PrenotazioneForm()

    return render(request, 'aggiungi_prenotazioni.html', {'form': form})



def dashboard_paziente(request):
    user_id = request.session.get("user_id")
    paziente = Paziente.objects.get(id_paziente=user_id)
    return render(request, 'dashboard_paziente.html', {'nome': paziente.nome})



def visualizza_prenotazione(request):

    user_id = request.session.get("user_id")
    prenotazioni = Prenotazione.objects.filter(id_paziente=user_id).prefetch_related(
        Prefetch(
            'esami',
            queryset=ListaEsami.objects.select_related('id_esame')
        )
    )




    # Mappa: Prenotazione → [Esami]
    prenotazioni_con_esami = {}

    for pren in prenotazioni:
        esami = [le.id_esame for le in pren.esami.all()]

        # Accesso diretto alla visita medica
        visita = pren.visita_medica  # Accesso diretto tramite related_name
        sede_nome = visita.sede.nome if visita.sede else "N.D."

        prenotazioni_con_esami[pren] = {
            "esami": esami,
            "sede": sede_nome
        }



    return render(request, 'visualizza_prenotazione.html', {'prenotazioni': prenotazioni_con_esami})



def visualizza_referti(request):
    if request.session.get("user_type") != "paziente":
        return redirect('login')

    paziente_id = request.session.get("user_id")

    referti = Prestazione.objects.filter(
        codice_visita__id_prenotazione__id_paziente=paziente_id,
        referto__isnull=False,
        data_prestazione__isnull=False
    ).select_related('id_esame', 'codice_visita__id_prenotazione')

    return render(request, 'visualizza_referti.html', {'referti': referti})

def visualizza_fatture(request):
    if request.session.get("user_type") != "paziente":
        return redirect("login")

    user_id = request.session.get("user_id")
    paziente = Paziente.objects.get(id_paziente=user_id)

    # Visite del paziente
    visite = VisitaMedica.objects.filter(id_prenotazione__id_paziente=paziente)
    fatture_da_mostrare = []



    #per ogni visita del paziente...
    for visita in visite:
        prestazioni = Prestazione.objects.filter(codice_visita=visita)

        # ...verifica che TUTTE le prestazioni abbiano referto
        if prestazioni.exists() and all(p.referto for p in prestazioni):
            # Imposta data_visita come la data dell'ultimo referto, se non impostata
            if not visita.data_visita:
                ultima_data = Prestazione.objects.filter(id_prestazione__in=prestazioni).aggregate(Max("data_prestazione"))["data_prestazione__max"]
                visita.data_visita = ultima_data
                visita.save()

            # Se non esiste ancora fattura per quella visita, creala
            if not Fattura.objects.filter(codice_visita=visita).exists():
                totale = prestazioni.aggregate(Sum("id_esame__costo"))["id_esame__costo__sum"] or 0
                Fattura.objects.create(
                    codice_visita=visita,
                    data_emissione=visita.data_visita,
                    id_paziente=paziente,
                    importo=totale
                )

            # Aggiungi la fattura esistente alla lista da mostrare
            fattura = Fattura.objects.get(codice_visita=visita)
            fatture_da_mostrare.append(fattura)


    return render(request, "fatture_paziente.html", {"fatture": fatture_da_mostrare})

def download_fattura_pdf(request, numero_fattura):
    from .models import Fattura

    fattura = Fattura.objects.get(numero_fattura= numero_fattura)
    template_path = 'fattura_pdf_template.html'  # deve esistere

    context = {'fattura': fattura}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="fattura_{numero_fattura}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Errore durante la generazione del PDF', status=500)

    return response

#FUNZIONI MEDICO

def dashboard_personale(request):
    user_id = request.session.get("user_id")
    personale = Personale.objects.get(id_personale=user_id)
    return render(request, 'dashboard_personale.html', {'nome': personale.nome})


def gestione_prestazioni(request):
    # Verifica se l'utente è personale (medico o tecnico)
    if request.session.get("user_type") != "personale":
        return redirect('login')

    personale_id = request.session.get("user_id")
    medico = Personale.objects.get(id_personale=personale_id)

    # Recupera solo prestazioni assegnate a questo medico, senza referto
    prestazioni = Prestazione.objects.filter(
        personale__id_personale=medico,
        referto__isnull=True
    ).select_related(
    'id_esame',
    'codice_visita__id_prenotazione__id_paziente'
).distinct()

    if request.method == 'POST':
        prestazione_id = request.POST.get('prestazione_id')
        data_referto = request.POST.get('data_referto')
        testo_referto = request.POST.get('testo_referto')

        if prestazione_id and data_referto and testo_referto:

            #prende data prenotazione per fare check data referto sia successiva a prenotazione..
            prestazione = Prestazione.objects.select_related(
                'codice_visita__id_prenotazione'
            ).get(id_prestazione=prestazione_id)

            data_prenotazione = prestazione.codice_visita.id_prenotazione.data_prenotazione

            # Converti la stringa in datetime.date (se arriva come stringa dal form)
            try:
                data_referto_date = datetime.strptime(data_referto, "%Y-%m-%d").date()
            except ValueError:
                messages.error(request, "Formato data non valido.")
                return redirect('gestione_prestazioni')
            #...qui dove fa il check
            if data_referto_date < data_prenotazione:
                messages.error(request, "La data della prestazione non può precedere la data della prenotazione.")
                return redirect('gestione_prestazioni')

            prestazione.data_prestazione = data_referto_date
            prestazione.referto = testo_referto
            prestazione.save()

            messages.success(request, "Referto salvato con successo!")

            # Redirect sulla stessa pagina per ricaricare la lista aggiornata
            return redirect('gestione_prestazioni')
        else:
            messages.error(request, "Tutti i campi sono obbligatori.")

    if not prestazioni.exists():
        messages.info(request, "Non ci sono prestazioni da refertare.")
        return redirect('dashboard_personale')

    return render(request, 'gestione_prestazioni.html', {'prestazioni': prestazioni})