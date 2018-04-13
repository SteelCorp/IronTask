from django.db import models

from irontask_app.models.Categorie import Categorie
from irontask_app.models.Triathlon import Triathlon


class Caracteriser(models.Model):
    """Class Representant le lien entre triathlon et catégorie (exemple 20 filles seniors pour triat Lyon"""

    nbrParticipant = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Caractériser"