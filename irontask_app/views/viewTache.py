from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig

from irontask_app.forms.AffecterForm import AffecterForm
from irontask_app.forms.TacheFrom import TacheForm
from irontask_app.models import Materiel, Triathlon
from django.core.paginator import Paginator
from django.contrib import messages
from irontask_app.models import Tache
from irontask_app.utils.decorators import triathlon_required
from datetime import date

from irontask_app.utils.tables import TachesTables


@login_required(login_url='login/')
@triathlon_required
def listTache(request):
    """Vue qui retourne la liste de toutes les taches"""

    table = TachesTables(Tache.objects.filter(fk_triathlon=request.session['idTriathlon']))
    RequestConfig(request, paginate={'per_page': 8}).configure(table)
    tacheForm = TacheForm()

    """ si méthode POST alors sauvegarder resultat du formulaire"""
    if request.method == 'POST':
        tacheForm = TacheForm(request.POST)

        if tacheForm.is_valid():
            tachem = tacheForm.save(commit=False)
            tachem.fk_triathlon = Triathlon.objects.get(id=request.session['idTriathlon'])
            tachem.save()
        else:
            """ Passe le message d'error du formulaire à la template
            afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, tacheForm.errors)
        return redirect(listTache)
    return render(request, 'tache/listTaches.html', {'table': table, 'form': tacheForm})


@login_required(login_url='login/')
@triathlon_required
def editerTache(request, id):
    tache = Tache.objects.get(id=id)
    tacheForm = TacheForm()

    if request.method == "POST":
        tacheForm = TacheForm(request.POST)

        if tacheForm.is_valid():
            tacheForm.save()

        return redirect('/')

    return render(request, 'tache/editerTache.html', {'form': tacheForm}, {'tache': tache})


@login_required(login_url='login/')
@triathlon_required
def getTache(request, id):
    affecterForm = AffecterForm()
    tache = Tache.objects.get(id=id)
    if request.method == 'POST':
        affecterForm = AffecterForm(request.POST)
        print(affecterForm.errors)
        if affecterForm.is_valid():
            affecter = affecterForm.save(commit=False)
            affecter.fk_tache = tache
            affecter.save()
    return render(request, 'tache/details_tache.html', {'tache': tache, 'affecterForm': AffecterForm})


@login_required(login_url='login/')
@triathlon_required
def deleteTache(request, id):
    Tache.filter(id=id).delete()

    return redirect('tache/listTache.html')


@login_required(login_url='login/')
def createTache(request):
    return render(request)
