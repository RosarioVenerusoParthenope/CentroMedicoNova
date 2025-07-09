# 🏥 Clinica Nova – Gestionale Medico in Django

[📄 Clicca qui per aprire la documentazione PDF completa](https://github.com/RosarioVenerusoParthenope/CentroMedicoNova/blob/main/Presentazione%20Progetto%20Clinica%20Nova/progetto%20clinica%20nova.pdf)

**Clinica Nova** è un’app web sviluppata in Django, pensata per simulare la gestione di una clinica: dalla prenotazione di esami alla refertazione, fino alla fatturazione. Il progetto è stato realizzato per fini didattici.

---

## ⚙️ Installazione (locale)

```bash
git clone https://github.com/RosarioVenerusoParthenope/CentroMedicoNova.git
cd CentroMedicoNova

# (Facoltativo) Ambiente virtuale
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

# Installazione dipendenze
pip install -r requirements.txt

# Migrazioni e avvio
python manage.py migrate
python manage.py runserver


📘 Manuale d’uso: come utilizzare l’app
👤 1. Accesso come Paziente
Vai su “Registrati” dalla homepage

Inserisci tutti i dati richiesti (nome, cognome, codice fiscale, ecc.)

Dopo la registrazione, effettua l’accesso come paziente

🗓️ 2. Prenotazione di esami
Vai su “Prenota visita”

Seleziona uno o più esami disponibili:

Ecocardiogramma

Elettrocardiogramma

RX torace

Spirometria

Test da sforzo

Risonanza magnetica

Ecografia addominale

Inserisci una descrizione (opzionale) e invia la prenotazione

⚠️ La data della visita sarà automaticamente impostata a un giorno successivo per semplicità.

📋 3. Visualizza le tue prenotazioni
Vai su “Le mie prenotazioni”

Troverai l’elenco delle tue visite prenotate con gli esami relativi

⚠️ Finché gli esami non sono stati refertati, non sarà visibile né il referto né la fattura.

🩺 4. Accesso come Medico per completare il flusso
🔍 Come sapere quale medico utilizzare?
Accedi come paziente

Vai su “Visite da effettuare”

Vedrai per ogni esame il medico assegnato automaticamente

🧑‍⚕️ Credenziali di accesso Medici (test):
Nome	Email	Password	Specializzazione
Luca	lrossi@clinica.it	luca123	Radiologia
Elena	eferrari@clinica.it	elena456	Radiologia
Chiara	cbianchi@clinica.it	chiara789	Cardiologia
Marco	mconti@clinica.it	marco321	Cardiologia
Alberto	averdi@clinica.it	alberto654	Pneumologia
Giulia	ggalli@clinica.it	giulia987	Medicina dello sport

✍️ 5. Scrittura dei referti
Fai logout come paziente

Accedi come medico assegnato

Vai su “Gestione prestazioni”

Qui vedrai solo gli esami a te assegnati e ancora da refertare

Compila il referto per ogni prestazione e salva

💡 Per test più semplici, prova con una sola prestazione. Il sistema è progettato anche per gestirne più in una singola prenotazione.

📄 6. Visualizzazione Referti e Fattura
Ritorna a loggarti come paziente

Vai su “I miei referti” per consultare i referti degli esami completati

Vai su “Visualizza fattura” per il riepilogo dei costi

Scarica la fattura in PDF per ciascuna visita completata

📌 Note Finali
⚠️ Il progetto è puramente dimostrativo. Alcune scelte (come l’assegnazione automatica dei medici o le date semplificate) sono state fatte per facilitare la comprensione del flusso.

🛠️ Possibili sviluppi futuri
Assegnazione manuale degli esami da parte di personale amministrativo

Chat/messaggistica tra medico e paziente

Modifica o cancellazione prenotazioni

Referti con allegati (es. immagini diagnostiche)

Dashboard più avanzata con filtri, ricerca, statistiche

Profilo utente con possibilità di modifica dati

👨‍💻 Autore
Rosario Veneruso
📧 rosariovenerusoparthenope@gmail.com

markdown
Copia
Modifica

---

### ✅ Aggiunta su GitHub

1. Vai sulla tua repo: [https://github.com/RosarioVenerusoParthenope/CentroMedicoNova](https://github.com/RosarioVenerusoParthenope/CentroMedicoNova)
2. Clicca **“Add file” > “Create new file”**
3. Inserisci `README.md` come nome del file
4. Incolla il contenuto qui sopra
5. Scrivi un messaggio di commit (es. `Aggiunta guida completa all'uso`)
6. Clicca **“Commit new file”**

Vuoi che ti preparo anche un badge carino per “📘 Documentazione disponibile” o vuoi aggiungere immagini (screenshot)? P
