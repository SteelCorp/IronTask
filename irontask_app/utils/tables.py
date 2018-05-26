from html import escape

from irontask_app.models import Sponsor, Intervenant, Benevole, Tache, Sponsoriser, Affecter
import django_tables2 as tables
from django.urls import reverse
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _



class SponsorTables(tables.Table):
    editer = tables.TemplateColumn(
        '<a href="{% url "getSponsor" record.pk %}"><img src=\'{% load  staticfiles %} {% static "img/eye-3x.png" %}\' / width="25"></a>',
        verbose_name=u'Voir', )




    class Meta:
        model = Sponsor
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout', 'siret'


class IntervenantTables(tables.Table):
    editer = tables.TemplateColumn(
        '<a href="{% url "getIntervenant" record.pk %}"><img src=\'{% load  staticfiles %} {% static "img/eye-3x.png" %}\' / width="25"></a>',
        verbose_name=u'Voir', )



    class Meta:
        model = Intervenant
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout', 'siret'


class BenevoleTables(tables.Table):
    editer = tables.TemplateColumn(
        '<a href="{% url "getBenevole" record.pk %}"><img src=\'{% load  staticfiles %} {% static "img/eye-3x.png" %}\' / width="25"></a>',
        verbose_name=u'Voir', )

    class Meta:
        model = Benevole
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout', 'id', 'sexe', 'status', 'siret', 'dateNaissance'



class BenevoleTacheTables(tables.Table):
    Supprimer = tables.TemplateColumn(
        '<a href="{% url "supprimerAffectation" record.pk %}"><img src=\'{% load  staticfiles %} {% static "img/x-3x.png" %}\' / width="25"></a>',
        verbose_name=u'Supprimer', )



    class Meta:
        model = Affecter
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'dateAjout', 'id', 'dateAjout', 'fk_tache'




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
    editer = tables.TemplateColumn(
        '<a href="{% url "getTache" record.pk %}"><img src=\'{% load  staticfiles %} {% static "img/eye-3x.png" %}\' / width="25"></a>',
        verbose_name=u'Voir', )

    class Meta:
        model = Tache
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'id', 'fk_triathlon', 'fk_benevole', 'description', 'dateRappel', 'dateAjout'


class TachesEnRetardTables(tables.Table):
    niveauPriorite = PriorityColumn()
    editer = tables.TemplateColumn(
        '<a href="{% url "getTache" record.pk %}"><img src=\'{% load  staticfiles %} {% static "img/eye-3x.png" %}\' / width="25"></a>',
        verbose_name=u'Voir', )

    class Meta:
        model = Tache
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"class": "table table-condensed table-striped table-hover"}
        exclude = 'id', 'fk_triathlon', 'fk_benevole', 'dateAjout'

class DonationTriathlonTables(tables.Table):
    class Meta:
        model = Sponsoriser
        template_name = 'django_tables2/bootstrap4.html'
        exclude = 'id', 'fk_triathlon'

class AffectationListeTables(tables.Table):
    class Meta:
        model = Affecter
        template_name = 'django_tables2/bootstrap4.html'
        exclude = 'id', 'fk_triathlon'



class BenevoleAffecterTables(tables.Table):
    editer = tables.TemplateColumn(
        '<a href="{% url "getBenevole" record.pk %}"><img src=\'{% load  staticfiles %} {% static "img/eye-3x.png" %}\' / width="25"></a>',
        verbose_name=u'Voir', )
    class Meta:
        model = Benevole
        template_name = 'django_tables2/bootstrap4.html'
        exclude = 'dateAjout', 'id', 'sexe', 'status', 'siret', 'dateNaissance'
