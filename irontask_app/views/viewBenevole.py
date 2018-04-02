from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from irontask_app.models import Intervenant, Benevole
from django.urls import reverse
from irontask_app.forms.BenevoleForm import BenevoleForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string





@login_required(login_url='login/')
def listBenevole(request):
    """Vue qui retourne la liste de tous les intervenant"""

    benevole = Benevole.objects.all()
    benevoleForm = BenevoleForm()

    if request.method == 'POST':

        benevoleForm = benevoleForm(request.POST)

        if BenevoleForm.is_valid():
            benevole = benevoleForm.save(commit=True)
            benevole.save()
        return redirect(listBenevole)
    return render(request, 'listBenevole.html', {'Benevole': benevole, 'form': benevoleForm})


"""""@login_required(login_url='login/')
def editerSponsor(request, siret):

    s = Sponsor.objects.get(siret=siret)
    sponsorForm = SponsorForm(instance=s)
    html = render_to_string('modalEditerSponsor.html', {'form': sponsorForm})



    if request.method == 'POST':
        s = Sponsor.objects.get(siret=siret)
        sponsorform = SponsorForm(request.POST, instance=s)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
            return redirect(listSponsor)
    return render(request, 'modalEditerSponsor.html', {'form' : sponsorForm})"""

def editerBenevole(request, pk=None):
    """Vue qui permet d'éditer un intervenant"""
    pass



def getBenevole(request, pk):
    """
    Vue qui retourne l'intervenant fournit en paramètre
    :param pk est la primary key d'un intervenant
    """
    pass


@login_required(login_url='login/')
def deleteBenevole(request, pk):
    """Vue qui permet de supprimer un intervenant
    :param pk est la primary key d'un intervenant
    """
    pass


@login_required(login_url='login/')
def createBenevole(request):
    """ Vue qui permet de creer un intervenant
    """
    pass
