from django.shortcuts import render, redirect
from irontask_app.models import Sponsoriser
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def listDonation(request):

    """vue qui return toutes les donations"""
    listDonation = Sponsoriser.objets.all()

    return render(request, 'donation.html', {'donation': listDonation})


def listDonationSponsor(request, idSponsor):
    """
    Vue qui retourne la list des donations pour un sponsors donné fournit en paramètre
    ::param fk_sponsoriser est l'id d'un sponsor
    """

    listDonationSponsor = Sponsoriser.objets.filter(fk_sponsoriser=idSponsor)

    return render(request, "viewSpo.html", {'donationSponsor': listDonationSponsor})


def listDonationTriathlon(request, idTriathlon):
    """
    Vue qui retourne la list des donations pour un sponsors donné fournit en paramètre
    ::param fk_triathlon est l'id d'un triathlon
    """

    listDonationTriathlon = Sponsoriser.objets.filter(fk_triathlon=idTriathlon)

    return render(request, "donationSponsor.html", {'listDonationTriathlon': listDonationTriathlon})