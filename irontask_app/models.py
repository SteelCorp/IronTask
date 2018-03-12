from django.db import models
from django.core.validators import RegexValidator


# Create your models here.



class Intervenant(models.Model):
    """
    Class Réprensentant un intervenant
    """
    siret = models.PositiveIntegerField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.PositiveSmallIntegerField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()


class Sponsor(models.Model):
    """
    Class Réprensentant un sponsor
    """

    siret = models.PositiveIntegerField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.CharField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()



    def __str__(self):
        """
        :return: String représentant l'objet Sponsor
        """
        return self.raisonSocial
