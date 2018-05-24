from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from irontask_app.models import Materiel
from irontask_app.forms.StockForm import StockForm
from django.core.paginator import Paginator
from django.contrib import messages
from irontask_app.models import Materiel
from irontask_app.utils.decorators import triathlon_required


@login_required(login_url='login/')
@triathlon_required
def listStock(request):
    """Vue qui retourne la liste de tous les sponsors"""

    stock = Materiel.objects.all()
    stockForm = StockForm()

    """ Implémentation de la pagination"""
    paginator = Paginator(stock, 2)
    page = request.GET.get('page')
    stock = paginator.get_page(page)

    """ si méthode POST alors sauvegarder resultat du formulaire"""
    if request.method == 'POST':
        stockForm = StockForm(request.POST)

        if stockForm.is_valid():
            stockForm.save(commit=True)
        else:
            """ Passe le message d'error du formulaire à la template
            afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, stockForm.errors)
        return redirect(listStock)
    return render(request, 'stocks/listStock.html', {'Stock': stock, 'form': stockForm})


@login_required(login_url='login/')
@triathlon_required
def editerStock(request):
    return render(request)


@login_required(login_url='login/')
@triathlon_required
def getStock(request, pk):
    stock = Materiel.objects.get(pk=pk)
    return render(request, 'stocks/voirStocks.html', {'Stock': stock})


@login_required(login_url='login/')
@triathlon_required
def deleteStock(request, pk):
    Materiel.objects.filter(pk=pk).delete()
    return redirect(listStock)


@login_required(login_url='login/')
@triathlon_required
def createStock(request):
    return render(request)
