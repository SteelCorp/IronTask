from django.db import models


class Materiel(models.Model):
    """
    Class Représentant le materiel
    """

    nom = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    qteTotal = models.PositiveIntegerField(blank=False, null=False)
    lieuStockage = models.CharField(max_length=50, blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        :return: String représentant l'objet Materiel par son nom et son lieu de stockage
        """
        return self.nom + ' stocké a : ' + self.lieuStockage