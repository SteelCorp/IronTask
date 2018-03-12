from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Sponsor

def listSponsor(request):
    """Vue qui retourne la liste de tous les sponsors"""

    sponsor = Sponsor.objects.all().filter()

    return render(request, 'listSponsor.html', {'Sponsor': sponsor})


def getSponsor(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un sponsor
    """
    sponsor = Sponsor.objets.get(siret = siret)

    return render(request, "Sponsor.html", locals())


def deleteSponsor(request, siret):
    sponsor = Sponsor.objects.get(siret=siret)
    sponsor.delete()
