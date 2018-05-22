from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from irontask_app.models import Triathlon, Sponsoriser, Sponsor
from irontask_app.forms.TriathlonForm import *
from irontask_app.urls import *
import datetime


def selectTriathlon(request, id):
    """Fonction qui met dans l'objet triathlon selectionner dans le cookies,
    l'id d'un triathlon afin de le reutiliser dans les autres vues
    """
    if request.session.get('idTriathlon'):
        request.session['idTriathlon'] = None
        request.session['idTriathlon'] = id
        return redirect('listTache')
    else:
        request.session['idTriathlon'] = id
        return redirect('/')


def choisirTriathlon(request):
    """Page redirige par le decorator triathlon_required, afin de forcer l'utilisateur
    à choisir un triathlon"""
    triathlons = Triathlon.objects.filter()

    return render(request, 'triathlon/choisirTriathlon.html', {'triathlons': triathlons})


def listTriathlon(request):
    """Vue qui retourne la liste de tous les triathlons"""

    listTriathlon = Triathlon.objets.all()

    return render(request, 'triatlon.html', {'triathlon': listTriathlon})


@login_required(login_url='login/')
def voirTriathlon(request, pk):
    """
    Vue qui retourne le triatlon fournit en paramètre
    ::param id est l'id d'un triathlon
    """
    triathlon = Triathlon.objects.get(pk=pk)
    nbrSponsor = Sponsor.objects.filter(sponsoriser__fk_triathlon=triathlon).count()

    return render(request, "triathlon/voirTriathlon.html", {'triathlon': triathlon, 'nbrSponsor': nbrSponsor})


@login_required(login_url='login/')
def editerTriathlon(request, pk):
    tria = Triathlon.objects.get(pk=pk)
    triathlonForm = TriathlonForm(instance=tria)

    if request.method == "POST":
        form = TriathlonForm(request.POST, instance=tria)
        if form.is_valid():
            form.save()

        return redirect('/')
    return render(request, 'triathlon/editerTriathlon.html', {"form": triathlonForm})


def ajouterTriathlon(request):
    if request.method == 'POST':
        tria = TriathlonForm(request.POST)
        if tria.is_valid():
            tria.save()

    return redirect('/')


def supprimerTriathlon(request, pk):
    Triathlon.objects.filter(pk=pk).delete()

    # Si le triathlon supprimer est dans le cookies, alors rétablir idTriathlon dans le cookies à None
    if pk == request.session['idTriathlon']:
        del request.session['idTriathlon']

    return redirect('/')
