from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django_tables2 import RequestConfig

from irontask_app.models import Sponsoriser, Triathlon
from django.contrib.auth.decorators import login_required
from irontask_app.forms.DonationForm import DonationForm
from django.contrib import messages
from irontask_app.utils.decorators import triathlon_required
from irontask_app.utils.tables import DonationTriathlonTables


@login_required(login_url='login/')
@triathlon_required
def listDonationSponsorsTriathlon(request, idSponsors):
    """vue qui return toutes les donations"""
    listDonationSponsorsTriathlon = Sponsoriser.objets.filter(fk_sponsoriser=idSponsors)
    donationForm = DonationForm

    if request.method == 'POST':
        donationForm = DonationForm(request.POST)

        if donationForm.is_valid():
            donation = donationForm.save(commit=False)
            donation.fk_triathlon = request.session['idTriathlon']
            donation.fk_sponsoriser = idSponsors
            donation.save()
        else:
            """ Passe le message d'error du formulaire à la template
             afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, DonationForm.errors)

        return redirect(listDonationSponsorsTriathlon)

    return render(request, 'donation.html', {'donation': listDonationSponsorsTriathlon})


@login_required(login_url='login/')
@triathlon_required
def ajouterDonation(request):
    """

    :param request:
    :return: Vue qui permet à la modal de faire une request de Type POST afin d'ajouter une donation
    """
    tria = Triathlon.objects.get(id=request.session['idTriathlon'])
    if request.method == 'POST':
        donationForm = DonationForm(request.POST)

        if donationForm.is_valid():
            donation = donationForm.save(commit=False)
            donation.fk_triathlon = tria
            donation.save()
            return HttpResponseRedirect('/personnel/sponsor/')
        return HttpResponseRedirect('/personnel/sponsor/')


@login_required(login_url='login/')
@triathlon_required
def listDonationSponsor(request, idSponsor):
    """
    Vue qui retourne la list des donations pour un sponsors donné fournit en paramètre
    ::param fk_sponsoriser est l'id d'un sponsor
    """

    listDonationSponsor = Sponsoriser.objets.filter(fk_sponsoriser=idSponsor)

    return render(request, "viewSpo.html", {'donationSponsor': listDonationSponsor})


@login_required(login_url='login/')
@triathlon_required
def listDonationTriathlon(request):
    """
    Vue qui retourne la list des donations pour un sponsors donné fournit en paramètre
    ::param fk_triathlon est l'id d'un triathlon
    """
    table = DonationTriathlonTables(Sponsoriser.objects.filter(fk_triathlon=request.session['idTriathlon']))
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    return render(request, "dashboard/listDonations.html", {'table' : table})
