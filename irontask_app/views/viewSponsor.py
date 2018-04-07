from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from irontask_app.models import Sponsor
from django.urls import reverse
from irontask_app.forms.SponsorForm import SponsorForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


@login_required(login_url='login/')
def listSponsor(request):
    """Vue qui retourne la liste de tous les sponsors"""

    sponsor = Sponsor.objects.all()
    sponsorForm = SponsorForm()

    if request.method == 'POST':

        sponsorform = SponsorForm(request.POST)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
        return redirect(listSponsor)
    return render(request, 'listSponsor.html', {'Sponsor': sponsor, 'form': sponsorForm })


@login_required(login_url='login/')
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
    return render(request, 'modalEditerSponsor.html', {'form' : sponsorForm})



def getSponsor(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un sponsor
    """
    sponsor = Sponsor.objects.get(siret=siret)

    return render(request, "voirSponsor.html", {'Sponsor': sponsor})


@login_required(login_url='login/')
def deleteSponsor(request, siret):
    sponsor = Sponsor.objects.get(siret=siret)
    sponsor.delete()
    sponsor.save()
    return redirect(reverse(viewname=listSponsor))


@login_required(login_url='login/')
def createSponsor(request):

    """
       :param request:
       :return:
       """

    return render(request, 'add_Sponsor.html', {'SponsorForm': SponsorForm})
