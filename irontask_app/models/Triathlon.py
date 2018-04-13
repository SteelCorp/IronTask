from django.db import models

from irontask_app.models.TypeTriathlon import TypeTriathlon


class Triathlon(models.Model):
    """Class Répresentant un Triathlon"""

    date = models.DateField(null=False, blank=False)
    heureDepart = models.TimeField(null=False, blank=False)
    codePostal = models.CharField(max_length=5, null=False, blank=False)
    adresse = models.CharField(max_length=50, null=False, blank=False)
    ville = models.CharField(max_length=50, null=False, blank=False)
    fk_TypeTriathlon = models.ForeignKey(TypeTriathlon, on_delete=models.PROTECT, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retourne une représentation string de l'objet Triathlon
        (utile pour la partie admin) """

        return 'Triathlon du ' + str(self.date) + ' à ' + self.ville

    class Meta:
        verbose_name_plural = "Triathlon"