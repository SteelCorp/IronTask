from django.shortcuts import render, redirect
from irontask_app.models import Sponsoriser
from django.contrib.auth.decorators import login_required
from irontask_app.forms.DonationForm import DonationForm
from django.contrib import messages

@login_required(login_url='login/')
def listDonationSponsorsTriathlon(request, idSponsors):
    """vue qui return toutes les donations"""
    listDonationSponsorsTriathlon = Sponsoriser.objets.filter(fk_sponsoriser=idSponsors)
    donationForm = DonationForm

    if request.method == 'POST':
        donationForm = DonationForm(request.POST)

        if donationForm.is_valid():
            donation = donationForm.save(commit=False)
            donation.fk_triathlon = request.session['id_Triathlon']
            donation.fk_sponsoriser = idSponsors
            donation.save()
        else:
            """ Passe le message d'error du formulaire à la template
             afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, DonationForm.errors)

        return redirect(listDonationSponsorsTriathlon)

    return render(request, 'donation.html', {'donation': listDonationSponsorsTriathlon})


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