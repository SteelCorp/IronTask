from django import template
from django.db.models import Sum

from irontask_app.models import *
from irontask_app.forms.TriathlonForm import *
from django.utils.translation import ugettext as _
import json
import datetime

register = template.Library()

@register.filter
def nbrTacheEnRetardPourTriathlon(session):
    return Tache.objects.filter(fk_triathlon=session, dateFin__lt =datetime.date.today()).count()

@register.filter
def nbrDonationPourTriatlon(session):
    return Sponsoriser.objects.filter(fk_triathlon=session).count()

@register.filter
def nbrTotalEurosPourTriatlon(session):
    somme = Sponsoriser.objects.filter(fk_triathlon=session).aggregate(Sum('donation'))['donation__sum']
    return somme

@register.filter
def nbrTachesPourTriathlon(session):
    return Tache.objects.filter(fk_triathlon=session).count()

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
