from django.shortcuts import render
from CentroMedico.form import PrenotazioneForm
from CentroMedico.models import *


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

            # Redirect a dashboard o conferma
            return redirect('dashboard_paziente')
    else:
        form = PrenotazioneForm()

    return render(request, 'aggiungi_prenotazione.html', {'form': form})
