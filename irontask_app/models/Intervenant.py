from django.db import models

from irontask_app.validators import phoneValidator


class Intervenant(models.Model):
    """
    Class Reprénsentant un intervenant
    """
    siret = models.CharField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, blank=False, null=True)
    type = models.CharField(max_length=50, blank=False, null=True)
    adresse = models.CharField(max_length=200, blank=False, null=True)
    codePostal = models.CharField(max_length=5, blank=False, null=True)
    ville = models.CharField(max_length=50, blank=False, null=True)
    telephoneFixe = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator])
    telephonePort = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator])
    email = models.EmailField(blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        :return: String représentant l'objet Intervenant par sa raison social
        """
        return self.raisonSocial