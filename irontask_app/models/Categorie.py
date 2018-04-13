from django.db import models


class Categorie(models.Model):
    """
    Class Reprénsentant une catégorie de triathlon

    age max peut etre nullable car une catégorie peux etre ouverte à toute age
    sexe est représenté sous forme de booléen pas soucie d'optimisation
    """

    SEX_CHOICES = (
        ('F', 'Feminin',),
        ('M', 'Masculin',),
    )
    libelle = models.CharField(max_length=50, blank=False, null=False)
    ageMin = models.PositiveSmallIntegerField(blank=False, null=False)
    ageMax = models.PositiveSmallIntegerField(blank=False, null=False)
    sexe = models.CharField(max_length=1, choices=SEX_CHOICES)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        :return: String représentant l'objet Catégorie par son libellé
        """
        return self.libelle

    class Meta:
        verbose_name_plural = "Catègories"