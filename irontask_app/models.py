from django.db import models
from irontask_app.validators import *
from django.contrib.auth.models import User




class UserProfile(models.Model):
    """
    Class pour la gestion des utilateurs du logiciel (connexion etc...)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # pagination_config = models.IntegerField(default=25)





class Intervenant(models.Model):
    """
    Class Reprénsentant un intervenant
    """
    siret = models.CharField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, blank=False, null=True)
    type = models.CharField(max_length=50, blank=False, null=True)
    adresse = models.CharField(max_length=200, blank=False, null=True)
    codePostal = models.CharField(max_length=5, blank=False, null=True)
    ville = models.CharField(max_length=50, blank=False, null=True)
    telephoneFixe = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator])
    telephonePort = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator])
    email = models.EmailField(blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)

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
    raisonSocial = models.CharField(max_length=50, blank=False, null=True)
    adresse = models.CharField(max_length=200, blank=False, null=True)
    codePostal = models.CharField(max_length=5, blank=False, null=True)
    ville = models.CharField(max_length=50, blank=False, null=True)
    telephoneFixe = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator])
    telephonePortable = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator])
    email = models.EmailField(blank=False, null=True)
    dateAjout = models.DateField(auto_now_add=True)

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
    ageMax = models.PositiveSmallIntegerField(blank=False, null=False)
    sexe = models.CharField(max_length=1, choices=SEX_CHOICES)
    dateAjout = models.DateField(auto_now_add=True)

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
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        :return: String représentant l'objet Materiel par son nom et son lieu de stockage
        """
        return self.nom + ' stocké a : ' + self.lieuStockage


class Benevole(models.Model):
    """Class Representant un bénévole"""
    SEX_CHOICES = (
        ('F','Feminin' ),
        ('M','Masculin'),

    )
    STATUS_CHOICES = (
        ('A', 'Administrateur'),
        ('O', 'Organisateur'),
        ('B', 'Benevole'),
    )

    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    dateNaissance = models.DateField(blank=False, null=True)
    sexe = models.CharField(choices=SEX_CHOICES, max_length=1, null=False)
    adresse = models.CharField(max_length=50, blank=False, null=True)
    codePostal = models.CharField(max_length=5, blank=False, null=True)
    ville = models.CharField(max_length=50, blank=False, null=True)
    telephoneFixe = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator])
    telephonePortable = models.CharField(max_length=10, blank=False, null=False, validators=[phoneValidator])
    email = models.EmailField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """String du benevole (lol)"""
        return 'Benevole :' + self.nom + " " + self.prenom


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


class Triathlon(models.Model):
    """Class Répresentant un Triathlon"""

    date = models.DateField(null=False, blank=False)
    heureDepart = models.TimeField(null=False, blank=False)
    codePostal = models.CharField(max_length=5, null=False, blank=False)
    adresse = models.CharField(max_length=50, null=False, blank=False)
    ville = models.CharField(max_length=50, null=False, blank=False)
    fk_TypeTriathlon = models.ForeignKey(TypeTriathlon, on_delete=models.PROTECT, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retourne une représentation string de l'objet Triathlon
        (utile pour la partie admin) """

        return 'Triathlon du ' + str(self.date) + ' à ' + self.ville


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


class Intervenir(models.Model):
    """Class Representant le lien entre triathlon et Intervenant"""

    devis = models.CharField(max_length=150)
    prixDevis = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_intervenant = models.ForeignKey(Intervenant, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)


class Sponsoriser(models.Model):
    """Class Representant le lien entre triathlon et Sponsor"""

    donation = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_sponsoriser = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)


class Caracteriser(models.Model):
    """Class Representant le lien entre triathlon et catégorie (exemple 20 filles seniors pour triat Lyon"""

    nbrParticipant = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)


class Allouer(models.Model):
    """Class Representant le lien caracterisant l'allocation d'un materiel pour un triathlon donné"""

    qteUtilise = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, null=False)
    fk_benevole = models.ForeignKey(Benevole, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (('fk_triathlon', 'fk_benevole'),)


class Affecter(models.Model):
    """Class Represantant le lien caractérisant entre benevole et tache"""

    fk_benevole = models.ForeignKey(Benevole, on_delete=models.CASCADE, null=False, blank=False)
    fk_tache = models.ForeignKey(Tache, on_delete=models.CASCADE, blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)
