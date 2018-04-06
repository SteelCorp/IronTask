from django import forms
from irontask_app.models import Benevole
from django.forms import ModelForm



class BenevoleForm(ModelForm):
    nom = forms.CharField(required=True, label="Nom", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    prenom = forms.CharField(required=True, label="Prénom", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    dateNaissance = forms.DateField(required=True, label="Date de naissance", widget=forms.TextInput(
                            attrs={"type": "text", "class": "form-control",
                                   "id": "formGroupExampleInput",
                                   "placeholder": ""}))
    sexe = forms.CharField(required=True, max_length=1, label="H/F", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    adresse = forms.CharField(max_length=5,label="Adresse", widget=forms.TextInput(
                            attrs={"type": "text", "class":"form-control",
                                            "id": "formGroupExampleInput",
                                            "placeholder":""}))
    codePostal = forms.CharField(label="Code Postal", widget=forms.TextInput(
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
        model = Benevole
        fields = '__all__'
