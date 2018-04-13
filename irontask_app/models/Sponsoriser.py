from django.db import models

from irontask_app.models.Sponsor import Sponsor
from irontask_app.models.Triathlon import Triathlon


class Sponsoriser(models.Model):
    """Class Representant le lien entre triathlon et Sponsor"""

    donation = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_sponsoriser = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Donations"