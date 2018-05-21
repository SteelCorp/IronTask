from irontask_app.models import Sponsor
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

class SponsorTables(tables.Table):
    class Meta:
        model = Sponsor

        template_name = 'django_tables2/bootstrap4.html'