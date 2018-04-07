from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import Sponsor, Sponsoriser
from django.urls import reverse
from irontask_app.forms.SponsorForm import SponsorForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required(login_url='login/')
def listSponsor(request):
    """Vue qui retourne la liste de tous les sponsors"""

    sponsor = Sponsor.objects.all()
    sponsorForm = SponsorForm()

    """ Implémentation de la pagination"""
    paginator = Paginator(sponsor, 2)
    page = request.GET.get('page')
    sponsor = paginator.get_page(page)

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
    return render(request, 'personnels/listSponsor.html', {'Sponsor': sponsor, 'form': sponsorForm, 'page': page, 'paginator': paginator})


@login_required(login_url='login/')
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
def getSponsor(request, siret):
    """
    Vue qui retourne le sponsor fournit en paramètre
    ::param siret est le siret d'un sponsor
    """
    sponsor = Sponsor.objects.get(siret=siret)
    listDonationSponsor = Sponsoriser.objects.filter(fk_sponsoriser=siret)

    return render(request, "personnels/voirSponsor.html", {'Sponsor': sponsor,  'listDonationSponsor': listDonationSponsor})


@login_required(login_url='login/')
def deleteSponsor(request, siret):
    sponsor = Sponsor.objects.get(siret=siret)
    sponsor.delete()
    sponsor.save()
    return redirect(reverse(viewname=listSponsor))


@login_required(login_url='login/')
def createSponsor(request):

    """
       :param request:
       :return:
       """

    return render(request, 'add_Sponsor.html', {'SponsorForm': SponsorForm})
