from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django_tables2 import RequestConfig

from irontask_app.forms.AffecterForm import AffecterForm
from irontask_app.forms.BenevoleForm import BenevoleForm
from irontask_app.forms.TacheFrom import TacheForm
from irontask_app.models import Materiel, Triathlon, Benevole, Affecter
from django.core.paginator import Paginator
from django.contrib import messages
from irontask_app.models import Tache
from irontask_app.utils.decorators import triathlon_required
import datetime

from irontask_app.utils.tables import TachesTables, AffectationListeTables, BenevoleTables, BenevoleTacheTables


def supprimer(request, pk):
    Affecter.objects.filter(pk=pk).delete()

    return redirect('/')