from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from irontask_app.models import Intervenant, Benevole
from django.urls import reverse
from irontask_app.forms.BenevoleForm import BenevoleForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from irontask_app.decorators import triathlon_required

@login_required(login_url='login/')
@triathlon_required
def listBenevole(request):
    """Vue qui retourne la liste de tous les intervenant"""

    benevole = Benevole.objects.all()
    benevoleForm = BenevoleForm()


    """ Implémentation de la pagination"""
    paginator = Paginator(benevole, 2)
    page = request.GET.get('page')
    benevole = paginator.get_page(page)

    if request.method == 'POST':
        benevoleForm = BenevoleForm(request.POST)

        if benevoleForm.is_valid():
            benevole = benevoleForm.save(commit=True)
            benevole.save()
        return redirect(listBenevole)
    return render(request, 'personnels/Benevole/listBenevole.html',
                  {'Benevole': benevole, 'form': benevoleForm, 'paginator': paginator})


@login_required(login_url='login/')
def editerBenevole(request, pk):
    benevole = Benevole.objects.get(pk=pk)
    benevoleForm = BenevoleForm(instance=benevole)

    if request.method == "POST":
        form = benevoleForm(request.POST, instance=benevole)
        if form.is_valid():
            form.save()

        return redirect('/')


    return render(request, 'personnels/Benevole/editerBenevole.html', {'form' : benevoleForm})





@login_required(login_url='login/')
@triathlon_required
def getBenevole(request, pk):
    """
    Vue qui retourne l'intervenant fournit en paramètre
    :param pk est la primary key d'un intervenant
    """

    benevole = Benevole.objects.get(pk=pk)

    return render(request, "personnels/Benevole/voirBenevole.html", {'Benevole': benevole})


@login_required(login_url='login/')
@triathlon_required
def deleteBenevole(request, pk):
    """Vue qui permet de supprimer un intervenant
    :param id est la primary key d'un intervenant
    """
    Benevole.objects.filter(pk=pk).delete()
    return redirect(reverse(viewname=listBenevole))


@login_required(login_url='login/')
@triathlon_required
def createBenevole(request):
    """ Vue qui permet de creer un intervenant
    """
    pass
