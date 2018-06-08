from django.forms import ModelForm
from django import forms
from irontask_app.models import Affecter, Benevole


class AffecterForm(ModelForm):
    fk_benevole = forms.ModelChoiceField(label='Bénévole', queryset=Benevole.objects.all(),
                                        widget=forms.Select(
                                            {"class": "custom-select", "id": "inputGroupSelect03"}))

    class Meta:
        model = Affecter
        exclude = {'fk_triathlon', 'fk_tache'}
