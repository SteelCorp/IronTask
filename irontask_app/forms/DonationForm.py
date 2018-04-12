from django.forms import ModelForm
from django import forms
from irontask_app.models import Sponsoriser


class DonationForm(ModelForm):

    donation =forms.IntegerField(label="Donation : ", widget=forms.TextInput({"type": "text", "class": "form-control",
                                                          "id": "formGroupExampleInput",
                                                          "placeholder": ""}))

    class Meta:
        model = Sponsoriser
        fields = '__all__'
