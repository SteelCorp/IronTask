from django import forms
from irontask_app.models import Sponsor
from django.forms import ModelForm


class SponsorForm(ModelForm):
    siret = forms.CharField(label="N° SIRET", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    raisonSocial = forms.CharField(label="Raison Social", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    adresse = forms.CharField(label="Adresse", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    codePostal = forms.CharField(max_length=5,label="Code Postal", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    ville = forms.CharField(label="Ville", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    telephoneFixe = forms.CharField(label="Téléphone Fixe", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    telephonePortable = forms.CharField(label="Téléphone Portable", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))

    class Meta:
        model = Sponsor
        fields = '__all__'
