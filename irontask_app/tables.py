from irontask_app.models import Sponsor, Intervenant, Benevole
import django_tables2 as tables
from django.urls import reverse
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _





class SponsorTables(tables.Table):
    editer = tables.LinkColumn('getSponsor', args=[A('pk')], text='voir')

    class Meta:
        model = Sponsor
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout',

class IntervenantTables(tables.Table):
    editer = tables.LinkColumn('getIntervenant', args=[A('pk')], text='voir')

    class Meta:
        model = Intervenant
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout',

class BenevoleTables(tables.Table):
    editer = tables.LinkColumn('getBenevole', args=[A('pk')], text='voir')

    class Meta:
        model = Benevole
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout', 'id', 'sexe', 'status'