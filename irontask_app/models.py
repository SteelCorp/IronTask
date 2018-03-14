from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Benevole(models.Model):
    """
    Class représentant un bénévole (un responsable est nécessairement un bénévole)
    """

    SEX_CHOICES = (
        ('F', 'Feminin',),
        ('M', 'Masculin',),
    )
    nom = models.CharField(max_length=50, blank=True, null=False)
    prenom = models.CharField(max_length=50, blank=True, null=False)
    dateNaissance = models.DateField(verbose_name="Date de naissance")
    sexe = models.CharField(max_length=1,choices=SEX_CHOICES, default='M')
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.PositiveSmallIntegerField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephoneFixe = models.PositiveIntegerField(max_length=12, blank=False, null=False,verbose_name="Téléphone fixe")
    telephonePort = models.PositiveIntegerField(max_length=12, blank=False, null=False,verbose_name="Téléphone portable")
    email = models.EmailField(unique=True)

class Intervenant(models.Model):
    """
    Class Reprénsentant un intervenant
    """
    siret = models.PositiveIntegerField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.PositiveSmallIntegerField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()

    def __str__(self):
        """
        :return: String représentant l'objet Intervenant par sa raison social
        """
        return self.raisonSocial


class Sponsor(models.Model):
    """
    Class Reprénsentant un sponsor
    """

    siret = models.PositiveIntegerField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.CharField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()


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
    ageMax = models.PositiveSmallIntegerField()
    sexe = models.BooleanField(choices=SEX_CHOICES)

    def __str__(self):
        """
        :return: String représentant l'objet Catégorie par son libellé
        """
        return self.libelle


class Materiel(models.Model):
    """
    Class Représentant le materiel
    """

    nom = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    qteTotal = models.PositiveIntegerField(blank=False, null=False)
    lieuStockage = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        """
        :return: String représentant l'objet Materiel par son nom et son lieu de stockage
        """
        return self.nom + ' stocké a : ' + self.lieuStockage
