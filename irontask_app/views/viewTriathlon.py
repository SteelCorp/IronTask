from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Triathlon


def listTriathlon(request):
    """Vue qui retourne la liste de tous les triathlons"""

    listTriathlon = Triathlon.objets.all()

    return render(request, 'triatlon.html', {'triathlon': listTriathlon})
