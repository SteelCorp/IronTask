from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from irontask_app.models import Triathlon
from irontask_app.forms.TriathlonForm import *
import datetime




def selectTriathlon(request, id):
    """Fonction qui met dans l'objet triathlon selectionner dans le cookies,
    l'id d'un triathlon afin de le reutiliser dans les autres vues
    """
    if request.session.get('idTriathlon'):
        request.session['idTriathlon'] = None
        request.session['idTriathlon'] = id
        return redirect('/')
    else:
        request.session['idTriathlon'] = id
        return redirect('/')


def choisirTriathlon(request):
    """Page redirige par le decorator triathlon_required, afin de forcer l'utilisateur
    à choisir un triathlon"""
    triathlons = Triathlon.objects.filter(date__gt=datetime.date.today())

    return render(request, 'triathlon/choisirTriathlon.html', {'triathlons': triathlons})


def listTriathlon(request):
    """Vue qui retourne la liste de tous les triathlons"""

    listTriathlon = Triathlon.objets.all()


    return render(request, 'triatlon.html', {'triathlon': listTriathlon})


@login_required(login_url='login/')

def voirTriathlon(request, pk):
    """
    Vue qui retourne le triatlon fournit en paramètre
    ::param id est l'id d'un triathlon
    """
    triathlon = Triathlon.objects.get(pk=pk)

    return render(request, "triathlon/voirTriathlon.html", {'triathlon': triathlon})

def editerTriathlon(request, pk):
    tria = Triathlon.objects.get(pk=pk)
    triathlonForm = TriathlonForm(instance=tria)
    return render(request, 'triathlon/editerTriathlon.html', {"form": triathlonForm})

def supprimerTriathlon(request, pk):
    Triathlon.objects.filter(pk=pk).delete()
    request.session['idTriathlon'] = None
    request.session.modified = True

    return redirect('/')



def ajouterTriathlon(request):

    if request.method == 'POST':
        tria = TriathlonForm(request.POST)
        print(tria.errors)
        print(tria)
        if tria.is_valid():

            tria.save()
            print(tria.errors)

    return redirect('/')