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
    sponsorForm = SponsorForm()

    if request.method == 'POST':

        sponsorform = SponsorForm(request.POST)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
        return redirect(listSponsor)
    return render(request, 'listSponsor.html', {'Sponsor': sponsor, 'form': sponsorForm})


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

def editerIntervenant(request, siret=None):

    data = serializers.serialize('json', Intervenant.objects.filter(siret=siret) )

    return HttpResponse(data)



def getIntervenant(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un intervenant
    """
    intervenant = Intervenant.objects.get(siret=siret)

    return render(request, "Intervenant.html", locals())


@login_required(login_url='login/')
def deleteIntervenant(request, siret):
    intervenant = Intervenant.objects.get(siret=siret)
    intervenant.delete()
    intervenant.save()
    return redirect(reverse(viewname=listIntervenant))


@login_required(login_url='login/')
def createIntervenant(request):
    """
       :param request:
       :return:
       """

    return render(request, 'add_Intervenant.html', {'IntervenantForm': IntervenantForm})
