from django.db import models

from irontask_app.models.Benevole import Benevole
from irontask_app.models.Tache import Tache


class Affecter(models.Model):
    """Class Represantant le lien caractérisant entre benevole et tache"""

    fk_benevole = models.ForeignKey(Benevole, on_delete=models.CASCADE, null=False, blank=False)
    fk_tache = models.ForeignKey(Tache, on_delete=models.CASCADE, blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Affectation des bénévoles"