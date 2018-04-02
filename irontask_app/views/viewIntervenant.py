from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from irontask_app.models import Intervenant
from django.urls import reverse
from irontask_app.forms.IntervenantForm import IntervenantForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


@login_required(login_url='login/')
def listIntervenant(request):
    """Vue qui retourne la liste de tous les intervenant"""

    intervenant = Intervenant.objects.all()
    intervenantForm = IntervenantForm()

    if request.method == 'POST':

        intervenantForm = intervenantForm(request.POST)

        if IntervenantForm.is_valid():
            intervenant = intervenantForm.save(commit=True)
            intervenant.save()
        return redirect(listIntervenant)
    return render(request, 'listIntervenant.html', {'Intervenant': intervenant, 'form': intervenantForm})


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

def editerIntervenant(request, pk=None):
    """Vue qui permet d'éditer un intervenant"""
    data = serializers.serialize('json', Intervenant.objects.filter(pk=pk) )

    return HttpResponse(data)



def getIntervenant(request, pk):
    """
    Vue qui retourne l'intervenant fournit en paramètre
    :param pk est la primary key d'un intervenant
    """
    intervenant = Intervenant.objects.get(pk=pk)

    return render(request, "personnel/Intervenant.html", locals())


@login_required(login_url='login/')
def deleteIntervenant(request, pk):
    """Vue qui permet de supprimer un intervenant
    :param pk est la primary key d'un intervenant
    """
    intervenant = Intervenant.objects.get(pk=pk)
    intervenant.delete()
    intervenant.save()
    return redirect(reverse(viewname=listIntervenant))


@login_required(login_url='login/')
def createIntervenant(request):
    """ Vue qui permet de creer un intervenant
    """
    return render(request, 'personnel/add_Intervenant.html', {'IntervenantForm': IntervenantForm})
