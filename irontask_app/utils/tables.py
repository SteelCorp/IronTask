from irontask_app.models import Sponsor, Intervenant, Benevole, Tache, Sponsoriser
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
        exclude = 'dateAjout', 'siret'


class IntervenantTables(tables.Table):
    editer = tables.LinkColumn('getIntervenant', args=[A('pk')], text='voir')

    class Meta:
        model = Intervenant
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout', 'siret'


class BenevoleTables(tables.Table):
    editer = tables.LinkColumn('getBenevole', args=[A('pk')], text='voir')

    class Meta:
        model = Benevole
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout', 'id', 'sexe', 'status', 'siret'


class PriorityColumn(tables.Column):
    """
    Class qui sert à colorer les cellules en fonction de leurs
    priorité
    """

    def render(self, value):
        if value == dict(Tache.NIV_PRIORITE).get('3'):
            self.attrs = {"td": {"bgcolor": "FF3333"}}

        elif value == dict(Tache.NIV_PRIORITE).get('2'):
            self.attrs = {"td": {"bgcolor": "FF8585"}}

        elif value == dict(Tache.NIV_PRIORITE).get('1'):
            self.attrs = {"td": {"bgcolor": "FFC299"}}

        elif value == dict(Tache.NIV_PRIORITE).get('0'):
            self.attrs = {"td": {"bgcolor": "FFE2CE"}}

        return value


class TachesTables(tables.Table):
    niveauPriorite = PriorityColumn()
    editer = tables.LinkColumn('getTache', args=[A('id')], text='voir')

    class Meta:
        model = Tache
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'id', 'fk_triathlon', 'fk_benevole'


class DonationTriathlonTables(tables.Table):
    class Meta:
        model = Sponsoriser
        template_name = 'django_tables2/bootstrap4.html'
        exclude = 'id', 'fk_triathlon'