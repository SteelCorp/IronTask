from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Sponsor
from irontask_app.forms.SponsorForm import SponsorForm





def listSponsor(request):
    """Vue qui retourne la liste de tous les sponsors"""

    sponsor = Sponsor.objects.all().filter()
    sponsorForm = SponsorForm()

    if request.method == 'POST':
        sponsorform = SponsorForm(request.POST)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
        return redirect(listSponsor)
    return render(request, 'listSponsor.html', {'Sponsor': sponsor, 'sponsorForm':sponsorForm})


def editerSponsor(request, siret):


    s = Sponsor.objects.get(siret = siret)
    sponsorForm = SponsorForm(instance=s)

    if request.method == 'POST':
        sponsorform = SponsorForm(request.POST, instance=s)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
        return render(request, 'editerSponsor.html', {'sponsorForm': sponsorForm})

    return render(request, 'editerSponsor.html', {'sponsorForm': sponsorForm})




def getSponsor(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un sponsor
    """
    sponsor = Sponsor.objects.get(siret=siret)

    return render(request, "Sponsor.html", locals())


def deleteSponsor(request, siret):
    sponsor = Sponsor.objects.get(siret=siret)
    sponsor.delete()


def createSponsor(request):
    """
       :param request:
       :return:
       """

    return render(request, 'add_Sponsor.html', {'SponsorForm': SponsorForm})

