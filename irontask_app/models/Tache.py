from django.db import models

from irontask_app.models.Benevole import Benevole
from irontask_app.models.Triathlon import Triathlon


class Tache(models.Model):
    """Class Representant une Tache"""
    """
    Fusion avec tache modèle
    """
    NIV_AVANCEMENT = (
        ('P', 'Plannifié'),
        ('E', 'En cours'),
        ('V', 'Validé'),
    )
    NIV_PRIOROTE = (
        ('0', 'Aucune'),
        ('1', 'Faible'),
        ('2', 'Moyen'),
        ('3', 'Important')
    )
    nomTache = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    dateDebut = models.DateField(null=False, blank=False)
    dateFin = models.DateField(null=False, blank=False)
    dateRappel = models.DateField(null=True, blank=False)
    niveauAvancement = models.CharField(max_length=1, choices=NIV_AVANCEMENT)
    niveauPriorite = models.CharField(max_length=1, choices=NIV_PRIOROTE)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.PROTECT, null=False)
    fk_benevole = models.ForeignKey(Benevole, on_delete=models.PROTECT, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retrourne une representation string de l'objet Tache"""

        return 'Tache date de fin :' + str(self.dateFin) + ' avec niveau d\'avancement :' + self.niveauAvancement

    class Meta:
        verbose_name_plural = "Tâches"