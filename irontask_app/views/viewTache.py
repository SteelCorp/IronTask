from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django_tables2 import RequestConfig

from irontask_app.forms.AffecterForm import AffecterForm
from irontask_app.forms.BenevoleForm import BenevoleForm
from irontask_app.forms.TacheForm import TacheForm
from irontask_app.models import Materiel, Triathlon, Benevole, Affecter
from django.core.paginator import Paginator
from django.contrib import messages
from irontask_app.models import Tache
from irontask_app.utils.decorators import triathlon_required
import datetime

from irontask_app.utils.tables import TachesTables, AffectationListeTables, BenevoleTables, BenevoleTacheTables


@login_required(login_url='login/')
@triathlon_required
def listTache(request):
    """

    :param request:
    :return:
    """

    table = TachesTables(Tache.objects.filter(fk_triathlon=request.session['idTriathlon']))
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    tacheForm = TacheForm()
    benevoleForm = BenevoleForm()

    """ si méthode POST alors sauvegarder resultat du formulaire"""
    if request.method == 'POST':
        benevoleForm = BenevoleForm(request.POST)

        if benevoleForm.is_valid():
            benevoleF = benevoleForm.save(commit=False)
            benevoleF .save()
            return render(request, 'tache/listTaches.html',
                          {'table': table, 'form': tacheForm, 'benevoleForm': benevoleForm, 'successful_submit': True})
        else:
            """ Passe le message d'error du formulaire à la template
            afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, tacheForm.errors)
        return redirect(listTache)
    return render(request, 'tache/listTaches.html', {'table': table, 'form': tacheForm, 'benevoleForm': benevoleForm, 'successful_submit': False})


@login_required(login_url='login/')
@triathlon_required
def editerTache(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    tache = Tache.objects.get(id=id)
    tacheForm = TacheForm(instance=tache)

    if request.method == "POST":
        form = TacheForm(request.POST, instance=tache)
        print(form.errors)

        if form.is_valid():
            form.save()

        return redirect('listTache')

    return render(request, 'tache/editerTache.html', {'form': tacheForm})


@login_required(login_url='login/')
@triathlon_required
def getTache(request, id):
    """

    :param request:
    :param id:
    :return:
    """


    table = BenevoleTacheTables(Affecter.objects.filter(fk_tache=id))
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    affecterForm = AffecterForm()


    tache = Tache.objects.get(id=id)
    if request.method == 'POST':
        affecterForm = AffecterForm(request.POST)
        if affecterForm.is_valid():
            try:
                affecter = affecterForm.save(commit=False)
                affecter.fk_tache = tache
                affecter.save()
            except IntegrityError:
                messages.add_message(request, messages.INFO, "Le Bénévole est déjà affecté à cette tâche")


            return redirect(reverse('getTache', kwargs={"id": id}))
    return render(request, 'tache/details_tache.html', {'tache': tache, 'affecterForm': AffecterForm, 'table' : table})


@login_required(login_url='login/')
@triathlon_required
def deleteTache(request, id):
    
    Tache.filter(id=id).delete()

    return redirect('tache/listTache.html')


@login_required(login_url='login/')
@triathlon_required
def ajouterTache(request):
    """

    :param request:
    :return: Vue qui permet à la modal de faire une request de Type POST afin d'ajouter une donation
    """
    tria = Triathlon.objects.get(id=request.session['idTriathlon'])
    if request.method == 'POST':
        tacheForm = TacheForm(request.POST)

        if tacheForm.is_valid():
            tache = tacheForm.save(commit=False)
            tache.fk_triathlon = tria
            tache.save()
            return HttpResponseRedirect('/tache/liste/')
        return HttpResponseRedirect('/tache/liste/')


def listTacheRetard(request):
    """

    :param request:
    :return:
    """

    table = TachesTables(Tache.objects.filter(fk_triathlon=request.session['idTriathlon'], dateFin__lt=datetime.date.today()))
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    tacheForm = TacheForm()
    benevoleForm = BenevoleForm()

    """ si méthode POST alors sauvegarder resultat du formulaire"""
    if request.method == 'POST':
        benevoleForm = BenevoleForm(request.POST)

        if benevoleForm.is_valid():
            benevoleF = benevoleForm.save(commit=False)
            benevoleF.save()
            return render(request, 'tache/listTaches.html',
                          {'table': table, 'form': tacheForm, 'benevoleForm': benevoleForm, 'successful_submit': True})
        else:
            """ Passe le message d'error du formulaire à la template
            afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, tacheForm.errors)
        return redirect(listTache)
    return render(request, 'tache/listTaches.html',
                  {'table': table, 'form': tacheForm, 'benevoleForm': benevoleForm, 'successful_submit': False})


def calendrierTache(request):
    """

    :param request:
    :return:
    """
    taches = Tache.objects.filter(fk_triathlon=request.session['idTriathlon'])

    return render(request, 'calendrier.html', {'taches':taches})