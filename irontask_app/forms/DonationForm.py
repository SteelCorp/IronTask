from django.forms import ModelForm
from django import forms
from irontask_app.models import Sponsor, Sponsoriser


class DonationForm(ModelForm):

    donation = forms.IntegerField(label="Donation : ", widget=forms.TextInput({"type": "text", "class": "form-control",
                                                          "id": "formGroupExampleInput",
                                                          "placeholder": ""}))
    fk_sponsor = forms.ModelChoiceField(label='Type de Triathlon', queryset=Sponsor.objects.all(),
                                              widget=forms.Select(
                                                  {"class": "custom-select", "id": "inputGroupSelect03"}))


    class Meta:
        model = Sponsoriser
        exclude = {'fk_triathlon'}
