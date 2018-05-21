from django.contrib import admin
from irontask_app.models import Intervenant, Sponsor, Categorie, Affecter, Caracteriser, Materiel, Benevole, \
    TypeTriathlon, Triathlon, Tache, Intervenir, Allouer, Sponsoriser


# Register your models here.

class IntervenantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Intervenant)


class SponsorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sponsor)


class CategorieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categorie)


class MaterielAdmin(admin.ModelAdmin):
    pass


admin.site.register(Materiel)


class BenevoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Benevole)


class TypeTriathlonAdmin(admin.ModelAdmin):
    pass


admin.site.register(TypeTriathlon)


class TriathlonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Triathlon)


class TacheAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tache)


class IntervenirAdmin(admin.ModelAdmin):
    pass


admin.site.register(Intervenir)


class SponsoriserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sponsoriser)


class CaracteriserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Caracteriser)


class AllouerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Allouer)


class AffecterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Affecter)
