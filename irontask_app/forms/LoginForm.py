from django import forms
from irontask_app.models import UserProfile


class ConnexionForm(forms.Form):
    """
    Pour la page de login
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Compte utilisateur'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
