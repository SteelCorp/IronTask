from django import template
from irontask_app.models import *
from django.utils.translation import ugettext as _
import json
import datetime

register = template.Library()

@register.simple_tag
def nbrDonationPourTriatlon():
    return Sponsoriser.objects.filter().count()

@register.simple_tag
def nbrTachesPourTriathlon():
    return Tache.objects.filter().count()

@register.simple_tag
def getTriathlonNonFini():
    triathlons = Triathlon.objects.all()
    return triathlons

