# 🏥 Clinica Nova – Gestionale Medico in Django

[📄 Clicca qui per aprire la documentazione PDF completa](https://github.com/RosarioVenerusoParthenope/CentroMedicoNova/blob/main/Presentazione%20Progetto%20Clinica%20Nova/progetto%20clinica%20nova.pdf)

Clinica Nova è un'applicazione web realizzata in Django per la gestione di una clinica medica. Il progetto ha finalità **didattiche** e punta a simulare il ciclo completo di gestione: dalla prenotazione, all'assegnazione del personale, refertazione, fino alla visualizzazione della fattura.

---

## ⚙️ Installazione

Per eseguire il progetto in locale:

```bash
git clone https://github.com/RosarioVenerusoParthenope/CentroMedicoNova.git
cd CentroMedicoNova

# Crea un ambiente virtuale (opzionale ma consigliato)
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# Installa le dipendenze
pip install -r requirements.txt

# Applica le migrazioni
python manage.py migrate

# Avvia il server
python manage.py runserver


👤 Accesso Paziente
I pazienti possono registrarsi dalla homepage. Una volta registrati e loggati possono:

Prenotare esami

Visualizzare le proprie prenotazioni

Consultare i referti (una volta compilati)

Scaricare le fatture in PDF

Esami disponibili:
Ecocardiogramma

Elettrocardiogramma

RX torace

Spirometria

Test da sforzo

Risonanza magnetica

Ecografia addominale

🩺 Accesso Medico
Per testare la funzionalità dei medici, accedi con una delle seguenti credenziali:

Nome	Email	Password	Specializzazione
Luca	lrossi@clinica.it	luca123	Radiologia
Elena	eferrari@clinica.it	elena456	Radiologia
Chiara	cbianchi@clinica.it	chiara789	Cardiologia
Marco	mconti@clinica.it	marco321	Cardiologia
Alberto	averdi@clinica.it	alberto654	Pneumologia
Giulia	ggalli@clinica.it	giulia987	Medicina dello sport

🔄 Come testare il ciclo completo
Registrati come paziente

Fai una prenotazione selezionando uno o più esami

Vai in “Visite da effettuare” per vedere a quali medici sono stati assegnati gli esami

Fai logout, entra con uno dei medici indicati

Accedi a “Gestione prestazioni” e compila i referti

Rientra come paziente per consultare i referti e scaricare la fattura

📌 Note Finali
⚠️ Il progetto è a scopo didattico, pertanto alcune logiche (es. assegnazione automatica dei medici, date fittizie) sono state semplificate per agevolare la comprensione del flusso.

🛠️ Possibili Estensioni
Gestione manuale delle assegnazioni da parte di personale amministrativo

Messaggistica tra medico e paziente

Dashboard migliorata con filtri, ricerca, e modifiche alle prenotazioni

Allegati nei referti (es. immagini)

Gestione profilo personale
