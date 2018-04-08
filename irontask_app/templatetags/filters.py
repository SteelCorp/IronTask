from django import template
from irontask_app.models import *
from django.utils.translation import ugettext as _
import json
import datetime

register = template.Library()

@register.filter
def nbrDonationPourTriatlon(idTriathlon):
    return Sponsoriser.objects.filter(fk_triathlon=idTriathlon).count()

@register.filter
def nbrTachesPourTriathlon(idTriatlon):
    return Tache.objects.filter(fk_triathlon=idTriatlon).count()

@register.simple_tag
def getTriathlonNonFini():
    triathlons = Triathlon.objects.all()
    return triathlons

