from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig

from irontask_app.models import Intervenant
from django.urls import reverse
from irontask_app.forms.IntervenantForm import IntervenantForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from irontask_app.decorators import triathlon_required
from irontask_app.tables import IntervenantTables


@login_required(login_url='login/')
@triathlon_required
def listIntervenant(request):
    """Vue qui retourne la liste de tous les intervenant"""

    intervenant = Intervenant.objects.all()
    intervenantForm = IntervenantForm()

    table = IntervenantTables(Intervenant.objects.all())
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    if request.method == 'POST':

        intervenantform = IntervenantForm(request.POST)

        if intervenantform.is_valid():
            intervenant = intervenantform.save(commit=True)
            intervenant.save()
        return redirect(listIntervenant)
    return render(request, 'personnels/Intervenant/listIntervenant.html',
                  {'Intervenant': intervenant, 'form': intervenantForm, 'table': table})


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


@login_required(login_url='login/')
@triathlon_required
def getIntervenant(request, siret):
    """
    Vue qui retourne l'intervenant fournit en paramètre
    :param siret est la primary key d'un intervenant
    """
    intervenant = Intervenant.objects.get(siret=siret)

    return render(request, "personnels/Intervenant/voirIntervenant.html", {'Intervenant': intervenant})


@login_required(login_url='login/')
@triathlon_required
def deleteIntervenant(request, siret):
    """Vue qui permet de supprimer un intervenant
    :param pk est la primary key d'un intervenant
    """
    Intervenant.objects.filter(siret=siret).delete()
    return redirect(reverse(viewname=listIntervenant))


@login_required(login_url='login/')
@triathlon_required
def createIntervenant(request):
    """ Vue qui permet de creer un intervenant
    """
    return render(request, 'personnel/add_Intervenant.html', {'IntervenantForm': IntervenantForm})
