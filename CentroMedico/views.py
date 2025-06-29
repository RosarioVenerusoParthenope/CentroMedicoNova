from django.shortcuts import render
from CentroMedico.form import PrenotazioneForm
from CentroMedico.models import *
from django.contrib import messages
from django.shortcuts import redirect


def home(request):

    return render(request, 'home.html')

def login(request):

    return render(request, 'login.html')


def login_auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Paziente.objects.get(email=email)
            if user.password == password:
                request.session['user_type'] = 'paziente'
                request.session['user_id'] = user.id_paziente
                context = {"nome": user.nome}
                return render(request, 'dashboard_paziente.html',context)
        except Paziente.DoesNotExist:
            pass

        try:
            user = Personale.objects.get(email=email)
            if user.password == password:
                request.session['user_type'] = 'personale'
                request.session['user_id'] = user.id_personale
                context = {"nome": user.nome}
                return render(request, 'dashboard_personale.html', context)
        except Personale.DoesNotExist:
            pass

        # Login fallito
        return render(request, 'login.html', {'error': 'Credenziali non valide'})


def aggiungi_prenotazione(request):

    if request.method == 'POST':
        form = PrenotazioneForm(request.POST)
        if form.is_valid():
            # Recupera dati dal form
            data = form.cleaned_data['data_prenotazione']
            sede = form.cleaned_data['sede']
            esami_selezionati = form.cleaned_data['esami']

            # Recupera paziente dalla sessione
            user_id = request.session.get("user_id")
            paziente = Paziente.objects.get(id_paziente=user_id)

            # Crea prenotazione
            prenotazione = Prenotazione.objects.create(
                data_prenotazione=data,
                id_paziente=paziente
            )

            # Collega esami alla prenotazione
            for esame in esami_selezionati:
                ListaEsami.objects.create(id_prenotazione=prenotazione, id_esame=esame)

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

    prenotazioni = Prenotazione.objects.all()

    for prenotazione in prenotazioni:

        lista_esami = ListaEsami.objects.filter(id_prenotazione=prenotazione.id_prenotazione)
        esami = [entry.id_esame for entry in lista_esami]
        print(esami)
        print("altrO ID PRENOTAZIONE")




    return render(request, 'visualizza_prenotazione.html', {'esami': lista_esami})