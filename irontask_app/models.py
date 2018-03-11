from django.db import models


# Create your models here.

class Triathlon(models.Model):
    """Class Répresentant un Triathlon"""

    date = models.DateField(null=False, blank=False, verbose_name='date')

    heureDepart = models.TimeField(null=False, blank=False, verbose_name='heureDepart')

    codePostal = models.CharField(max_length=5, null=False, blank=False, verbose_name='codePostal')

    adresse = models.CharField(max_length=50, null=False, blank=False, verbose_name='adresse')

    ville = models.CharField(max_length=50, null=False, blank=False, verbose_name='ville')

    taches = models.ForeignKey(Tache, on_delete=models.CASCADE)
    # à coder la class Tache pour referencer la clé étrangère

    typeTriathlon = models.ForeignKey(TypeTriathlon, on_delete=models.PROTECT)

    # à coder la class TypeTriathlon pour referencer la clé étrangère

    def __str__(self):
        """Retourne une représentation string de l'objet Triathlon
        (utile pour la partie admin) """

        return 'Triathlon du ' + self.date + ' à ' + self.ville


class Sponsor(models.Model):
    """
    Class Réprensentant un sponsor
    """
    siret = models.CharField(max_length=14, primary_key=True, verbose_name='Siret', blank=False, null=False)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    adresse = models.CharField(max_length=50, blank=False, null=False)
    codePostal = models.CharField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField

    def __str__(self):
        """
        :return: String représentant l'objet Sponsor
        """
        return self.raisonSocial
