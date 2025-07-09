# 🏥 Clinica Nova – Gestionale Medico in Django

[📄 **Clicca qui per aprire la documentazione PDF completa**](https://github.com/RosarioVenerusoParthenope/CentroMedicoNova/blob/main/Presentazione%20Progetto%20Clinica%20Nova/progetto%20clinica%20nova.pdf)

---

## ⚙️ Installazione dell’applicazione

<details>
<summary>🔽 Clona il progetto</summary>

```bash
git clone https://github.com/RosarioVenerusoParthenope/CentroMedicoNova.git
cd CentroMedicoNova

</details> <details> <summary>🧪 (Opzionale) Crea ambiente virtuale</summary>

python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

</details> <details> <summary>📦 Installa le dipendenze</summary>

pip install -r requirements.txt

</details> <details> <summary>🚀 Applica le migrazioni e avvia il server</summary>

python manage.py migrate
python manage.py runserver

</details>
🔗 Apri http://127.0.0.1:8000 nel browser per utilizzare l’app.


### 👤 Accesso Paziente

I pazienti possono registrarsi direttamente dalla homepage.

Una volta registrati e loggati, possono:

- 📝 Prenotare uno o più esami  
- 📅 Visualizzare lo storico delle prenotazioni  
- 📄 Consultare i referti (una volta compilati)  
- 🧾 Scaricare le fatture in PDF  

#### Esami disponibili:

- Ecocardiogramma  
- Elettrocardiogramma  
- RX torace  
- Spirometria  
- Test da sforzo  
- Risonanza magnetica  
- Ecografia addominale



####🔄 Flusso completo da testare
####1️⃣ Registrati come paziente
Vai su “Registrati”, inserisci i dati e accedi con il tuo account.

####2️⃣ Prenota un esame
Vai su "Prenota visita"

-Seleziona uno o più esami disponibili
-Inserisci eventuali dettagli aggiuntivi
-Conferma

💡 Per test veloci puoi selezionare anche un solo esame.

####3️⃣ Controlla a quale medico sei stato assegnato
Dopo la prenotazione, vai su "Visite da effettuare"

Vedrai l’elenco dei medici assegnati ai tuoi esami

####4️⃣ Esegui il login come medico
Per refertare gli esami, effettua il logout da paziente e accedi con una delle seguenti credenziali:

<table> <thead> <tr> <th>Nome</th><th>Email</th><th>Password</th><th>Specializzazione</th> </tr> </thead> <tbody> <tr><td>Luca</td><td>lrossi@clinica.it</td><td>luca123</td><td>Radiologia</td></tr> <tr><td>Elena</td><td>eferrari@clinica.it</td><td>elena456</td><td>Radiologia</td></tr> <tr><td>Chiara</td><td>cbianchi@clinica.it</td><td>chiara789</td><td>Cardiologia</td></tr> <tr><td>Marco</td><td>mconti@clinica.it</td><td>marco321</td><td>Cardiologia</td></tr> <tr><td>Alberto</td><td>averdi@clinica.it</td><td>alberto654</td><td>Pneumologia</td></tr> <tr><td>Giulia</td><td>ggalli@clinica.it</td><td>giulia987</td><td>Medicina dello sport</td></tr> </tbody> </table>
####5️⃣ Vai su “Gestione prestazioni” e compila il referto
Ogni medico vedrà solo gli esami che gli sono stati assegnati

Per ogni esame, clicca su “Scrivi referto”, compila e salva


####6️⃣ Ritorna come paziente
-Dopo che tutti i referti sono compilati, il paziente può:
-Visualizzare i referti
-Scaricare la fattura PDF


📌 Note
⚠️ Questo progetto è a scopo didattico. Alcune logiche (es. date e assegnazione automatica medici) sono state semplificate per rendere il sistema più accessibile e testabile.

