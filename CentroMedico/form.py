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

