from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Triathlon


def listTriathlon(request):
    """Vue qui retourne la liste de tous les triathlons"""

    listTriathlon = Triathlon.objets.all()

    return render(request, 'triatlon.html', {'triathlon': listTriathlon})


def getTriathlon(request, id):
    """
    Vue qui retourne le triatlon fournit en paramètre
    ::param id est l'id d'un triathlon
    """
    triathlon = Triathlon.objets.get(id=id)

    return render(request, "triatlon.html", {'triathlon': triathlon})
