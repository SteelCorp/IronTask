from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Sponsor, Sponsoriser, Triathlon
from django.urls import reverse
from irontask_app.forms.SponsorForm import SponsorForm
from irontask_app.forms.DonationForm import DonationForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator
from irontask_app.decorators import triathlon_required



@login_required(login_url='login/')
@triathlon_required
def listSponsor(request):
    """Vue qui retourne la liste de tous les sponsors"""

    tria = Triathlon.objects.get(id=request.session['idTriathlon'])

    """Donne les sponsors affecter au triathlon courant"""
    sponsor = Sponsor.objects.filter(sponsoriser__fk_triathlon=tria)
    

    # Instancie le formulaire sponsorForm
    sponsorForm = SponsorForm()
    donationForm = DonationForm()


    """ Implémentation de la pagination"""
    paginator = Paginator(sponsor, 25)
    page = request.GET.get('page')
    sponsor = paginator.get_page(page)

    #Si le requeste est de type POST
    if request.method == 'POST':
        sponsorform = SponsorForm(request.POST)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
        else:
            """ Passe le message d'error du formulaire à la template
             afin de l'afficher en cas d'erreur dans le formulaire"""
            messages.add_message(request, messages.INFO, sponsorform.errors)

        return redirect(listSponsor)
    return render(request, 'personnels/Sponsor/listSponsor.html', {'Sponsor': sponsor,
                                                           'form': sponsorForm, 'page': page,
                                                           'paginator': paginator, 'donationForm':donationForm})


@login_required(login_url='login/')
@triathlon_required
def editerSponsor(request, siret):

    s = Sponsor.objects.get(siret=siret)
    sponsorForm = SponsorForm(instance=s)
    html = render_to_string('personnels/modalEditerSponsor.html', {'form': sponsorForm})


    if request.method == 'POST':
        s = Sponsor.objects.get(siret=siret)
        sponsorform = SponsorForm(request.POST, instance=s)

        if sponsorform.is_valid():
            sponsor = sponsorform.save(commit=True)
            sponsor.save()
            return redirect(listSponsor)
    return render(request, 'personnels/modalEditerSponsor.html', {'form' : sponsorForm})


@login_required(login_url='login/')
@triathlon_required
def getSponsor(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un sponsor
    """
    sponsor = Sponsor.objects.get(siret=siret)
    listDonationSponsor = Sponsoriser.objects.filter(fk_sponsor=siret)
    donationForm = DonationForm

    """ si méthode POST alors sauvegarder resultat du formulaire"""
    if request.method == 'POST':
        donationForm = DonationForm(request.POST)


        if donationForm.is_valid():
            """
            si le formulaire est valide alors on ne commit pas de suite car il n'y a que donation dans donationForm            
            """
            donation = donationForm.save(commit=False)
            """ obligé de passer idTriathlon dans l'objet triat idem avec spon pour enregister dans donation"""
            triat = Triathlon.objects.get(id=request.session['idTriathlon'])
            spon = Sponsor.objects.get(siret=siret)
            donation.fk_triathlon = triat
            donation.fk_sponsoriser = spon
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

