from django import template
from irontask_app.models import *
from django.utils.translation import ugettext as _
import json
import datetime

register = template.Library()

def nbrDonationPourTriatlon(idTriathlon):
    return Sponsoriser.objects.filter(fk_triathlon=idTriathlon).count()


def nbrTachesPourTriathlon(idTriatlon):
    return Tache.objects.filter(fk_triathlon=idTriatlon).count()


register.filter('nbrDonationPourTriathlon', nbrDonationPourTriatlon)
register.filter('nbrTachesPourTriathlon', nbrTachesPourTriathlon)