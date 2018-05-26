from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Sponsor, Sponsoriser, Triathlon
from django.urls import reverse
from irontask_app.forms.SponsorForm import SponsorForm
from irontask_app.forms.DonationForm import DonationForm, DonationFormSansSponsor
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator
from irontask_app.utils.decorators import triathlon_required
from irontask_app.utils.tables import SponsorTables
from django_tables2 import RequestConfig


@login_required(login_url='login/')
@triathlon_required
def listSponsor(request):
    """Vue qui retourne la liste de tous les sponsors"""
    tria = Triathlon.objects.get(id=request.session['idTriathlon'])

    """Donne les sponsors affecter au triathlon courant"""
    sponsor = Sponsor.objects.filter()

    table = SponsorTables(Sponsor.objects.filter())
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    # Instancie le formulaire sponsorForm
    sponsorForm = SponsorForm()
    donationForm = DonationForm()

    # Si le requeste est de type POST
    if request.method == 'POST':
        sponsorform = SponsorForm(request.POST)

        if sponsorform.is_valid():

            sponsor = sponsorform.save(commit=True)
            sponsor.save()


        else:
            """ Passe le message d'error du formulaire à la template
             afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, sponsorform.errors)

        # Si le premier formulaire et valide, recharge la page avec la variable sccessful_submit à True, afin de réouvrir la modal d'ajout de donations
        return render(request, 'personnels/Sponsor/listSponsor.html', {'Sponsor': sponsor,
                                                                       'form': sponsorForm, 'table': table,
                                                                       'donationForm': donationForm,
                                                                       'successful_submit': True})

    return render(request, 'personnels/Sponsor/listSponsor.html', {'Sponsor': sponsor,
                                                                   'form': sponsorForm, 'table': table,
                                                                   'donationForm': donationForm, 'successful_submit': False})


@login_required(login_url='login/')
@triathlon_required
def editerSponsor(request, siret):
    s = Sponsor.objects.get(siret=siret)
    sponsorForm = SponsorForm(instance=s)

    if request.method == 'POST':
        s = Sponsor.objects.get(siret=siret)
        sponsorform = SponsorForm(request.POST, instance=s)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
            return redirect(listSponsor)
    return render(request, 'personnels/Sponsor/editerSponsor.html', {'form': sponsorForm})


@login_required(login_url='login/')
@triathlon_required
def getSponsor(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un sponsor
    """
    sponsor = Sponsor.objects.get(siret=siret)
    listDonationSponsor = Sponsoriser.objects.filter(fk_sponsor=siret)
    donationForm = DonationFormSansSponsor()



    """ si méthode POST alors sauvegarder resultat du formulaire"""
    if request.method == 'POST':
        donationForm = DonationFormSansSponsor(request.POST)
        donationForm.fk_sponsor = sponsor

        if donationForm.is_valid():
            """
            si le formulaire est valide alors on ne commit pas de suite car il n'y a que donation dans donationForm            
            """
            donation = donationForm.save(commit=False)
            """ obligé de passer idTriathlon dans l'objet triat idem avec spon pour enregister dans donation"""
            triat = Triathlon.objects.get(id=request.session['idTriathlon'])
            spon = Sponsor.objects.get(siret=siret)
            donation.fk_triathlon = triat
            donation.fk_sponsor = spon
            donation.save()
        else:
            """ Passe le message d'error du formulaire à la template"""
            """afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, DonationForm.errors)

    return render(request, "personnels/Sponsor/voirSponsor.html", {'sponsor': sponsor,
                                                                   'listDonationSponsor': listDonationSponsor,
                                                                   'donationForm': donationForm
                                                                   })


@login_required(login_url='login/')
@triathlon_required
def deleteSponsor(request, siret):
    Sponsor.objects.filter(siret=siret).delete()
    return redirect(reverse(viewname=listSponsor))


@login_required(login_url='login/')
@triathlon_required
def deleteDonation(request, idDonation):
    Sponsoriser.objects.filter(id=idDonation).delete()
    return redirect('/')
