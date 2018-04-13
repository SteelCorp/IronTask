from django.db import models

from irontask_app.models.Intervenant import Intervenant
from irontask_app.models.Triathlon import Triathlon


class Intervenir(models.Model):
    """Class Representant le lien entre triathlon et Intervenant"""

    devis = models.CharField(max_length=150)
    prixDevis = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_intervenant = models.ForeignKey(Intervenant, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Intervenir"