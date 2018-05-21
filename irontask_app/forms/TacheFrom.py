from django.forms import ModelForm
from django import forms
from irontask_app.models import Tache


class TacheForm(ModelForm):
    nom = forms.CharField(label="Nom", widget=forms.TextInput({"type": "text", "class": "form-control",
                                                               "id": "formGroupExampleInput",
                                                               "placeholder": ""}))
    description = forms.CharField(label="Description", widget=forms.TextInput({"type": "text", "class": "form-control",
                                                                 "id": "formGroupExampleInput",
                                                                 "placeholder": ""}))
    dateDebut = forms.CharField(widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))
    dateFin = forms.CharField(widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))
    dateRappel = forms.CharField(widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))

    niveauavancement = forms.IntegerField(label="Niveau Avancement",
                                  widget=forms.TextInput({"type": "text", "class": "form-control",
                                                          "id": "formGroupExampleInput",
                                                          "placeholder": ""}))
    niveauPriorite= forms.IntegerField(label="Niveau Priorité",
                                          widget=forms.TextInput({"type": "text", "class": "form-control",
                                                                  "id": "formGroupExampleInput",
                                                                  "placeholder": ""}))
    dateAjout = forms.CharField(widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))



    class Meta:
        model = Tache
        exclude = {'fk_benevole','fk_triathlon'}
