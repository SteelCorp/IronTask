from django.forms import ModelForm
from django import forms
from irontask_app.models import Materiel


class StockForm(ModelForm):
    nom = forms.CharField(label="Nom", widget=forms.TextInput({"type": "text", "class": "form-control",
                                                               "id": "formGroupExampleInput",
                                                               "placeholder": ""}))
    type = forms.CharField(label="Type", widget=forms.TextInput({"type": "text", "class": "form-control",
                                                                 "id": "formGroupExampleInput",
                                                                 "placeholder": ""}))
    qteTotal = forms.IntegerField(label="Quantité totale",
                                  widget=forms.TextInput({"type": "text", "class": "form-control",
                                                          "id": "formGroupExampleInput",
                                                          "placeholder": ""}))
    lieuStockage = forms.CharField(label="Lieu de stockage",
                                   widget=forms.TextInput({"type": "text", "class": "form-control",
                                                           "id": "formGroupExampleInput",
                                                           "placeholder": ""}))

    class Meta:
        model = Materiel
        fields = '__all__'
