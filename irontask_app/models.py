from django.db import models
from irontask_app.utils.validators import *
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
    siret = models.CharField(max_length=14, primary_key=True, verbose_name='Siret')
    raisonSocial = models.CharField(max_length=50, blank=False, null=True, verbose_name='Raison Social')
    type = models.CharField(max_length=50, blank=False, null=True, verbose_name='Type')
    adresse = models.CharField(max_length=200, blank=False, null=True, verbose_name='Adresse')
    codePostal = models.CharField(max_length=5, blank=False, null=True, verbose_name='Code Postal')
    ville = models.CharField(max_length=50, blank=False, null=True, verbose_name='Ville')
    telephoneFixe = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator], verbose_name='Téléphone Fixe')
    telephonePort = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator], verbose_name='Téléphone Portable')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        :return: String représentant l'objet Intervenant par sa raison social
        """
        return self.raisonSocial

    class Meta:
        verbose_name_plural = "Intervenant"


class Sponsor(models.Model):
    """
    Class Reprénsentant un sponsor
    """

    siret = models.CharField(max_length=14, primary_key=True, verbose_name='Siret')
    raisonSocial = models.CharField(max_length=50, blank=False, null=True, verbose_name='Raison Social')
    adresse = models.CharField(max_length=200, blank=False, null=True, verbose_name='Adresse')
    codePostal = models.CharField(max_length=5, blank=False, null=True, verbose_name='Code Postal')
    ville = models.CharField(max_length=50, blank=False, null=True, verbose_name='Ville')
    telephoneFixe = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator],
                                     verbose_name='Téléphone Fixe')
    telephonePortable = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator],
                                         verbose_name='Téléphone Portable')
    email = models.EmailField(blank=False, null=True, verbose_name='Email')
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.raisonSocial

    class Meta:
        verbose_name_plural = "Sponsor"


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
        verbose_name_plural = "Catégories"


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

    class Meta:
        verbose_name_plural = "Matériel"


class Benevole(models.Model):
    """Class Representant un bénévole"""
    SEX_CHOICES = (
        ('F', 'Feminin'),
        ('M', 'Masculin'),

    )


    nom = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nom')
    prenom = models.CharField(max_length=50, blank=False, null=False, verbose_name='Prénom')
    dateNaissance = models.DateField(blank=False, null=True, verbose_name='Date de naissance')
    sexe = models.CharField(choices=SEX_CHOICES, max_length=1, null=False, verbose_name='Adresse')
    adresse = models.CharField(max_length=50, blank=False, null=True, verbose_name='Adresse')
    codePostal = models.CharField(max_length=5, blank=False, null=True, verbose_name='Code postal')
    ville = models.CharField(max_length=50, blank=False, null=True, verbose_name='Ville')
    telephoneFixe = models.CharField(max_length=10, blank=False, null=True, validators=[phoneValidator], verbose_name='Téléphone Fixe')
    telephonePortable = models.CharField(max_length=10, blank=False, null=False, validators=[phoneValidator], verbose_name='Téléphone portable')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retourne un string representant le benevole"""
        return self.nom + " " + self.prenom

    class Meta:
        verbose_name_plural = "Bénévole"


class TypeTriathlon(models.Model):
    """Class representant un type de triathlon"""

    libelle = models.CharField(max_length=50, blank=False, null=False)
    distanceNatation = models.PositiveIntegerField(blank=False, null=False)
    distanceCyclisme = models.PositiveIntegerField(blank=False, null=False)
    distanceCourseAPied = models.PositiveIntegerField(blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retourne un string des parametre du type de triathlon"""
        return self.libelle

    class Meta:
        verbose_name_plural = "Type Triathlon"


class Triathlon(models.Model):
    """Class Répresentant un Triathlon"""

    date = models.DateField(null=False, blank=False, verbose_name='Date')
    description = models.TextField(verbose_name='Description')
    heureDepart = models.TimeField(null=False, blank=False, verbose_name='Heure de départ')
    codePostal = models.CharField(max_length=5, null=False, blank=False, verbose_name='Code postal')
    adresse = models.CharField(max_length=50, null=False, blank=False, verbose_name='Adresse')
    ville = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ville')
    fk_TypeTriathlon = models.ForeignKey(TypeTriathlon, on_delete=models.PROTECT, null=False, verbose_name='Type de Triathlon')
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retourne une représentation string de l'objet Triathlon
        (utile pour la partie admin) """

        return 'Triathlon du ' + str(self.date) + ' à ' + self.ville

    class Meta:
        verbose_name_plural = "Triathlon"


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
    NIV_PRIORITE = (
        ('0', 'Aucune'),
        ('1', 'Faible'),
        ('2', 'Moyen'),
        ('3', 'Important')
    )
    nomTache = models.CharField(max_length=150, verbose_name='Titre')
    description = models.TextField(verbose_name='Description')
    dateDebut = models.DateField(null=False, blank=False, verbose_name='Date de début')
    dateFin = models.DateField(null=False, blank=False, verbose_name='Date de fin')
    dateRappel = models.DateField(null=True, blank=False, verbose_name='Date de rappel')
    niveauAvancement = models.CharField(max_length=1, choices=NIV_AVANCEMENT, verbose_name="Niveau d'avancement")
    niveauPriorite = models.CharField(max_length=1, choices=NIV_PRIORITE, verbose_name='Priorité')
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.PROTECT, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        """Retrourne une representation string de l'objet Tache"""

        return 'Tache date de fin :' + str(self.dateFin) + ' avec niveau d\'avancement :' + self.niveauAvancement

    class Meta:
        verbose_name_plural = "Tâches"


class Intervenir(models.Model):
    """Class Representant le lien entre triathlon et Intervenant"""

    devis = models.CharField(max_length=150, verbose_name='Devis')
    prixDevis = models.PositiveIntegerField(null=False, blank=False, verbose_name='Prix')
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_intervenant = models.ForeignKey(Intervenant, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Intervenir"


class Sponsoriser(models.Model):
    """Class Representant le lien entre triathlon et Sponsor"""

    donation = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.donation) + "€ de " + self.fk_sponsor.__str__() + " pour le " + self.fk_triathlon.__str__()

    class Meta:
        verbose_name_plural = "Donations"


class Caracteriser(models.Model):
    """Class Representant le lien entre triathlon et catégorie (exemple 20 filles seniors pour triat Lyon"""

    nbrParticipant = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Caractériser"


class Allouer(models.Model):
    """Class Representant le lien caracterisant l'allocation d'un materiel pour un triathlon donné"""

    qteUtilise = models.PositiveIntegerField(null=False, blank=False)
    fk_triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE, null=False)
    fk_materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, null=False)
    fk_benevole = models.ForeignKey(Benevole, on_delete=models.CASCADE, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (('fk_triathlon', 'fk_benevole'),)
        verbose_name_plural = "Allocation du matériel"


class Affecter(models.Model):
    """Class Represantant le lien caractérisant entre benevole et tache"""

    fk_benevole = models.ForeignKey(Benevole, on_delete=models.CASCADE, null=False, blank=False)
    fk_tache = models.ForeignKey(Tache, on_delete=models.CASCADE, blank=False, null=False)
    dateAjout = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fk_benevole.__str__() + " affecter à la tâche id :" + str(self.fk_tache.id)

    class Meta:
        verbose_name_plural = "Affectation des bénévoles"
