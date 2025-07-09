from django import forms
from CentroMedico.models import Sede, Esame

class PrenotazioneForm(forms.Form):
    data_prenotazione = forms.DateField(   widget=forms.DateInput(attrs={'type': 'date'})  )
    sede = forms.ModelChoiceField(queryset=Sede.objects.all(), label="Sede")
    esami = forms.ModelMultipleChoiceField(
        queryset=Esame.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Seleziona esami"
)


class RegistrazioneForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    cognome = forms.CharField(label="Cognome", max_length=100)
    data_nascita = forms.DateField(label="Data di Nascita", widget=forms.DateInput(attrs={'type': 'date'}))
    codice_fiscale = forms.CharField(label="Codice Fiscale", max_length=16)

    sesso = forms.ChoiceField(
        label="Sesso",
        choices=[('M', 'Maschio'), ('F', 'Femmina')],
        widget=forms.RadioSelect
    )

    email = forms.EmailField(label="Email", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))