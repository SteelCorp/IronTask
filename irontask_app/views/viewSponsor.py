from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Sponsor

def listSponsor(request):
    """Vue qui retourne la liste de tous les sponsors"""

    listTriathlon = Sponsor.objets.all()

    return render(request, 'Sponsor.html', {'Sponsor': Sponsor})


def getSponsor(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un triathlon
    """
    triathlon = Sponsor.objets.get(siret = siret)

    return render(request, "Sponsor.html", {'Sponsor': Sponsor})


def deleteSponsor(request, siret):
    sponsor = Sponsor.objects.get(siret=siret)
    sponsor.delete()
