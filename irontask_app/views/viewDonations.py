from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from irontask_app.models import Intervenant, Benevole, Triathlon, Sponsor, Sponsoriser
from django.urls import reverse
from irontask_app.forms.BenevoleForm import BenevoleForm
from irontask_app.forms.SponsorForm import SponsorForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from irontask_app.decorators import triathlon_required
from django.contrib import messages


@login_required(login_url='login/')
@triathlon_required
def listDonations(request):
    """Vue qui retourne la liste de tous les sponsors"""

    tria = Triathlon.objects.get(id=request.session['idTriathlon'])

    """Donne les sponsors affecter au triathlon courant"""
    sponsor = Sponsoriser.objects.filter(fk_triathlon=tria)

    # Instancie le formulaire sponsorForm
    sponsorForm = SponsorForm()


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

        return redirect(listDonations)
    return render(request, 'donations/listDonations.html', {'Sponsor': sponsor,
                                                           'form': sponsorForm, 'page': page,
                                                           'paginator': paginator})