from django.forms import ModelForm
from django import forms
from irontask_app.models import Intervenir, Intervenant


class DevisForm(ModelForm):

    fk_intervenant = forms.ModelChoiceField(label='Type de Triathlon', queryset=Intervenant.objects.all(),
                                        widget=forms.Select(
                                            {"class": "custom-select", "id": "inputGroupSelect03"}))
    class Meta:
        model = Intervenir
        exclude = {'fk_triathlon'}
