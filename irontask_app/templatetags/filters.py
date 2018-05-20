from django import template
from irontask_app.models import *
from irontask_app.forms.TriathlonForm import *
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
    triathlons = Triathlon.objects.filter(date__gt=datetime.date.today())
    return triathlons

@register.filter
def getTriathlonEnCours(session):
    triathlon = Triathlon.objects.get(pk=session)
    return triathlon

@register.simple_tag
def triathlon_form():
    """ Permet d'inclure le formulaire d'ajout d'un triathlon dans toutes les pages"""
    return TriathlonForm

@register.simple_tag
def retard(ladate):
    if ladate < datetime.date.today():
        return True
    else:
        return False
