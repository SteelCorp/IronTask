from django.db import models


class TypeTriathlon(models.Model):
    """Class representant un type de triathlon"""

    libelle = models.CharField(max_length=50, blank=False, null=False)
    distanceNatation = models.PositiveIntegerField(blank=False, null=False)
    distanceCyclisme = models.PositiveIntegerField(blank=False, null=False)
    distanceCourseAPied = models.PositiveIntegerField(blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retourne un string des parametre du type de triathlon"""
        return 'Type triathlon de libelle ' + self.libelle