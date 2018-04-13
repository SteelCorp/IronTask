from django.db import models

from irontask_app.models.Benevole import Benevole
from irontask_app.models.Materiel import Materiel
from irontask_app.models.Triathlon import Triathlon


class Allouer(models.Model):
    """Class Representant le lien caracterisant l'allocation d'un materiel pour un triathlon donné"""

    qteUtilise = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, null=False)
    fk_benevole = models.ForeignKey(Benevole, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (('fk_triathlon', 'fk_benevole'),)
        verbose_name_plural = "Allocation du matériel"