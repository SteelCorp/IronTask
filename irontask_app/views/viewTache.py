from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from irontask_app.forms.TacheFrom import TacheForm
from irontask_app.models import Materiel, Triathlon
from django.core.paginator import Paginator
from django.contrib import messages
from irontask_app.models import Tache
from irontask_app.decorators import triathlon_required
from datetime import date

@login_required(login_url='login/')
@triathlon_required
def listTache(request):
    """Vue qui retourne la liste de toutes les taches"""

    tache = Tache.objects.all()
    tacheForm = TacheForm()

    print("mmmmmmm")

    """ si méthode POST alors sauvegarder resultat du formulaire"""
    if request.method == 'POST':
        tacheForm = TacheForm(request.POST)
        print("eeekmlk")

        print(request.session['id_Triathlon'])
        print("eeekmlk2")

        if tacheForm.is_valid():
            tachem = tacheForm.save(commit=False)
            tachem.fk_triathlon = request.session['id_Triathlon']
            print("eeee")
            print(request.session['id_Triathlon'])
            print("eeee2")

            tachem.save()
        else:
            """ Passe le message d'error du formulaire à la template
            afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, tacheForm.errors)
        return redirect(listTache)
    return render(request, 'tache/listTache.html', {'Tache': tache, 'form': tacheForm})


@login_required(login_url='login/')
@triathlon_required
def editerTache(request):

    return render(request)

@login_required(login_url='login/')
@triathlon_required
def getTache(request,pk):
    tache = Materiel.objects.get(pk=pk)
    return render(request, 'tache/voirTache.html', {'Tache': tache})


@login_required(login_url='login/')
@triathlon_required
def deleteTache(request):
    return render(request)

@login_required(login_url='login/')
def createTache(request):
    return render(request)