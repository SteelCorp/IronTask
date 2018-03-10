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