from django.forms import ModelForm
from django import forms
from irontask_app.models import Triathlon, TypeTriathlon

class TriathlonForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "id":"message-text2", "rows":"3"}))
    date = forms.CharField(widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))
    heureDepart = forms.CharField(widget=forms.TextInput({"class": "form-control", "type": "text", "value":"18:00"}))
    codePostal = forms.CharField(max_length=5, widget=forms.TextInput({"class":"form-control col-3", "type":"text", "value":"99999"}))
    adresse = forms.CharField(max_length=50, widget=forms.TextInput({"class":"form-control", "type":"text", "value":"Adresse"}))
    ville = forms.CharField(max_length=50, widget=forms.TextInput({"type":"text", "class":"form-control", "value":"Ville", "id":"villeTriatlhon"}))
    fk_TypeTriathlon = forms.ModelChoiceField(label='Type de Triathlon', queryset=TypeTriathlon.objects.all(), widget=forms.Select({"class":"custom-select", "id":"inputGroupSelect03"}))

    class Meta:
        model = Triathlon
        exclude = {'dateAjout',}


