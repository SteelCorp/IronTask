from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    Class pour la gestion des utilateurs du logiciel (connexion etc...)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # pagination_config = models.IntegerField(default=25)