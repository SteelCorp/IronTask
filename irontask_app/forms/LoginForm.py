from django import forms
from irontask_app.models import UserProfile


class ConnexionForm(forms.Form):
    """
    Pour la page de login
    """
    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)
