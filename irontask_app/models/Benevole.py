from django.db import models

from irontask_app.validators import phoneValidator


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