from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig

from irontask_app.models import Intervenant, Benevole, Triathlon
from django.urls import reverse
from irontask_app.forms.BenevoleForm import BenevoleForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from irontask_app.utils.decorators import triathlon_required
from irontask_app.utils.tables import BenevoleTables, BenevoleAffecterTables

from django_tables2 import RequestConfig


@login_required(login_url='login/')
@triathlon_required
def listBenevole(request):
    """Vue qui retourne la liste de tous les intervenant"""

    benevoleForm = BenevoleForm()

    table = BenevoleTables(Benevole.objects.all())
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    if request.method == 'POST':
        benevoleForm = BenevoleForm(request.POST)

        if benevoleForm.is_valid():
            benevole = benevoleForm.save(commit=True)
            benevole.save()
        return redirect(listBenevole)
    return render(request, 'personnels/Benevole/listBenevole.html',
                  {'form': benevoleForm, 'table': table})


@login_required(login_url='login/')
@triathlon_required
def editerBenevole(request, pk):
    bene = Benevole.objects.get(pk=pk)
    benevoleForm = BenevoleForm(instance=bene)

    if request.method == "POST":
        form = BenevoleForm(request.POST, instance=bene)

        if form.is_valid():
            form.save()

        return redirect('listBenevole')

    return render(request, 'personnels/Benevole/editerBenevole.html', {'form': benevoleForm})


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
    :param pk est la primary key d'un intervenant
    """
    Benevole.objects.filter(pk=pk).delete()
    return redirect(reverse(viewname=listBenevole))


@login_required(login_url='login/')
@triathlon_required
def createBenevole(request):
    """ Vue qui permet de creer un intervenant
    """
    pass




@login_required(login_url='login/')
@triathlon_required
def listBenevoleAffecter(request):
    """Vue qui retourne la liste de tous les intervenant"""


    triathlon = Triathlon.objects.get(id=request.session['idTriathlon'])
    table = BenevoleAffecterTables(Benevole.objects.filter(affecter__fk_tache__fk_triathlon=triathlon))
    RequestConfig(request, paginate={'per_page': 8}).configure(table)


    return render(request, 'dashboard/listBenevolesAffectes.html',
                  {'table': table})