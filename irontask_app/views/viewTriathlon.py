from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Triathlon
from django.contrib.auth.decorators import login_required


def selectTriathlon(request, id):
    """Fonction qui met dans l'objet cookies,
    l'id d'un triathlon afin de le reutiliser dans les autres vues
    """
    if request.session.get('idTriathlon'):
        request.session['idTriathlon'] = None
        request.session.pop('idTriathlon', id)
    else:
        request.session.pop('idTriathlon', id)

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
