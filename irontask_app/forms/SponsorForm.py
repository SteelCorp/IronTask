from django import forms
from irontask_app.models import Sponsor
from django.forms import ModelForm

class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'
