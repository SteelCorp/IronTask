from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import datetime




class UserProfile(models.Model):
    """
    Class pour la gestion des utilateurs du logiciel (connexion etc...)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #pagination_config = models.IntegerField(default=25)



class Intervenant(models.Model):
    """
    Class Reprénsentant un intervenant
    """
    siret = models.CharField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.CharField(max_length=5, blank=False, null=False)
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

    siret = models.CharField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.CharField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.raisonSocial



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




class Tache(models.Model):
    """Class Representant une Tache"""

    NivPriorite = (
        ('0', 'Aucune'),
        ('1', 'Faible'),
        ('2', 'Moyen'),
        ('3', 'Important')
    )
    DateFin = models.DateField(null=False, blank=False, verbose_name='DateFin')

    NiveauAvancement = models.CharField(max_length=1, choices=NivPriorite)

    Triathlon = models.ForeignKey(Triathlon, on_delete=models.PROTECT)

    #Benevole = models.ForeignKey(Benevole, on_delete=models.PROTECT)

    # TacheModel = models.ForeignKey(TacheModel, on_delete=models.PROTECT)

    def __str__(self):
        """Retrourne une representation string de l'objet Tache"""

        return 'Tache date de fin :' + self.DateFin + ' avec niveau d\'avancement :' + self.NiveauAvancement


class TypeTriathlon(models.Model):
    """Class representant un type de triathlon"""

    # id???

    libelle = models.CharField(max_length=50, blank=False, null=False)

    distanceNatation = models.PositiveIntegerField(blank=False, null=False)

    distanceCyclisme = models.PositiveIntegerField(blank=False, null=False)

    distanceCourseAPied = models.PositiveIntegerField(blank=False, null=False)

    # triathlon = models.ForeignKey(Triathlon, on_delete=) ???

    def __str__(self):
        """Retourne un string des parametre du type de triathlon"""
        return 'Type triathlon de libelle ' + self.libelle + ' Natation' + self.distanceNatation + ' Cyclisme ' + self.distanceCyclisme + ' Course ' + self.distanceCourseAPied


class Triathlon(models.Model):
    """Class Répresentant un Triathlon"""

    date = models.DateField(null=False, blank=False, verbose_name='date')

    heureDepart = models.TimeField(null=False, blank=False, verbose_name='heureDepart')

    codePostal = models.CharField(max_length=5, null=False, blank=False, verbose_name='codePostal')

    adresse = models.CharField(max_length=50, null=False, blank=False, verbose_name='adresse')

    ville = models.CharField(max_length=50, null=False, blank=False, verbose_name='ville')

    taches = models.ForeignKey(Tache, on_delete=models.CASCADE)
    # à coder la class Tache pour referencer la clé étrangère

    typeTriathlon = models.ForeignKey(TypeTriathlon, on_delete=models.PROTECT)
    # à coder la class TypeTriathlon pour referencer la clé étrangère

    def __str__(self):
        """Retourne une représentation string de l'objet Triathlon
        (utile pour la partie admin) """

        return 'Triathlon du ' + self.date + ' à ' + self.ville


class Benevole(models.Model):
    """Representation d'un benevole"""

    SEX_CHOICES = (
        ('F', 'Feminin',),
        ('M', 'Masculin',),
    )

    STATUS_CHOICES =(
        ('A', 'Administrateur'),
        ('O', 'Organisateur'),
        ('B', 'Benevole'),
    )

    Nom = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nom')

    Prenom = models.CharField(max_length=50, blank=False, null=False,verbose_name='Prenom')

    DateNaissance = models.DateField(blank=False, null=False, verbose_name='Date de naissance')

    Sexe = models.BooleanField(choices=SEX_CHOICES,verbose_name='Sexe')

    Adresse = models.CharField(max_length=50, blank=False, null=False,verbose_name='Adresse')

    CodePostal = models.CharField(max_length=5, blank=False, null=False, verbose_name='Code Postal')

    Ville = models.CharField(max_length=50, blank=False, null=False,verbose_name='Ville')

    TelephoneFixe = models.CharField(max_length=10, blank=False, null=False, verbose_name='Telephone Fixe')

    TelephonePortable = models.CharField(max_length=10, blank=False, null=False, verbose_name='Telephone Portable')

    Email = models.EmailField(verbose_name='Email')

    Status = models.CharField(max_length=1, choices=STATUS_CHOICES,verbose_name='Status')

    def __str__(self):
        """String du benevole (lol)"""
        return 'Benevole :' +self.Nom+" "+self.Prenom+' Status'+ self.STATUS_CHOICES

    
