from django.db import models

class CartellaClinica(models.Model):
    id_cartella = models.AutoField(primary_key=True)
    data_apertura = models.DateField(null=True)
    note = models.TextField(null=True)

class Paziente(models.Model):
    id_paziente = models.AutoField(primary_key=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()
    codice_fiscale = models.CharField(max_length=16, unique=True)
    sesso = models.CharField(max_length=1)
    id_cartella_clinica = models.OneToOneField(CartellaClinica, on_delete=models.CASCADE,related_name='paziente', null=True, blank=True)

class Sede(models.Model):
    codice_sede = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    via = models.CharField(max_length=100)
    città = models.CharField(max_length=100)
    CAP = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Prenotazione(models.Model):
    id_prenotazione = models.AutoField(primary_key=True)
    data_prenotazione = models.DateField()
    id_paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, related_name='prenotazioni')

class Personale(models.Model):
    id_personale = models.AutoField(primary_key=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()
    ruolo = models.CharField(max_length=100)
    specializzazione = models.CharField(max_length=100, null=True)

class Esame(models.Model):
    id_esame = models.AutoField(primary_key=True)
    nome_esame = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome_esame



class VisitaMedica(models.Model):
    codice_visita = models.AutoField(primary_key=True)
    data_visita = models.DateField(null=True, blank=True)
    id_prenotazione = models.OneToOneField(Prenotazione, on_delete=models.CASCADE, related_name='visita_medica')
    id_cartella_clinica = models.ForeignKey(CartellaClinica, on_delete=models.CASCADE, related_name='visite_mediche',null=True, blank=True)
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, related_name='sede',null=True, blank=True)

class Prestazione(models.Model):
    id_prestazione = models.AutoField(primary_key=True)
    data_prestazione = models.DateField(null=True, blank=True)
    referto = models.TextField(null=True)
    id_esame = models.ForeignKey(Esame, on_delete=models.CASCADE, related_name='prestazioni')
    codice_visita = models.ForeignKey(VisitaMedica, on_delete=models.CASCADE, related_name='prestazioni')

class Fattura(models.Model):
    numero_fattura = models.AutoField(primary_key=True)
    data_emissione = models.DateField()
    importo = models.DecimalField(max_digits=8, decimal_places=2)
    codice_visita = models.OneToOneField(VisitaMedica,on_delete=models.CASCADE,related_name='fattura')
    id_paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, related_name='fatture')

class ListaEsami(models.Model):
    id_prenotazione = models.ForeignKey(Prenotazione, on_delete=models.CASCADE, related_name='esami')
    id_esame = models.ForeignKey(Esame, on_delete=models.CASCADE, related_name='prenotazioni')

    class Meta:
        unique_together = (('id_prenotazione', 'id_esame'),)

class PersonalePrestazione(models.Model):
    id_personale = models.ForeignKey(Personale, on_delete=models.CASCADE, related_name='prestazioni')
    id_prestazione = models.ForeignKey(Prestazione, on_delete=models.CASCADE, related_name='personale')

    class Meta:
        unique_together = (('id_personale', 'id_prestazione'),)
