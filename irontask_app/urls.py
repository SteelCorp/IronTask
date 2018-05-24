from django.contrib import admin
from django.urls import path
from irontask_app.views import viewSponsor, viewIndex, viewLogin, \
    viewIntervenant, viewBenevole, viewStock, viewTriathlon, viewTache, viewSponsorDonation, viewAffecter
from django.conf.urls import url


from irontask_app import views

admin.site.site_header = 'IronTask Administration'
urlpatterns = [

    # Gestion de la session
    url('login/', viewLogin.user_login),
    url('logout/', viewLogin.logout_user, name='logout_user'),
    path('', viewIndex.index, name='index'),

    # Gestion des sponsors
    path('personnel/sponsor/', viewSponsor.listSponsor, name='listSponsor'),
    path('personnel/sponsor/get/<siret>/', viewSponsor.getSponsor, name='getSponsor'),
    path('personnel/sponsor/editer/<siret>/', viewSponsor.editerSponsor, name='editerSponsor'),
    path('personnel/sponsor/supprimer/<siret>/', viewSponsor.deleteSponsor, name='deleteSponsor'),

    # Gestion des donations
    path('personnel/donation/', viewSponsor.listSponsor, name='listDonation'),
    path('personnel/donation/ajouter/', viewSponsorDonation.ajouterDonation, name='ajouterDonation'),
    path('personnel/donation/get/<id>/', viewSponsor.getSponsor, name='getDonation'),
    path('personnel/donation/editer/<id>/', viewSponsor.editerSponsor, name='editerDonation'),
    path('personnel/donation/supprimer/<id>/', viewSponsor.deleteDonation, name='deleteDonation'),

    # Gestion des intervenants
    path('personnel/intervenant/', viewIntervenant.listIntervenant, name='listIntervenant'),
    path('personnel/intervenant/get/<siret>/', viewIntervenant.getIntervenant, name='getIntervenant'),
    path('personnel/intervenant/supprimer/<siret>/', viewIntervenant.deleteIntervenant, name='deleteIntervenant'),
    path('personnel/intervenant/ajouterDevis/', viewIntervenant.ajouterDevis, name='ajouterDevis'),



    # Gestion des benevoles
    path('personnel/benevole/', viewBenevole.listBenevole, name='listBenevole'),
    path('personnel/benevole/get/<pk>/', viewBenevole.getBenevole, name='getBenevole'),
    path('personnel/benevole/editer/<pk>/', viewBenevole.editerBenevole, name='editerBenevole'),
    path('personnel/benevole/supprimer/<pk>/', viewBenevole.deleteBenevole, name='deleteBenevole'),

    # Gestion des stocks
    path('stock/total/', viewStock.listStock, name='listStock'),
    path('stock/total/get/<pk>/', viewStock.getStock, name='getStock'),
    path('stock/total/editer/<pk>/', viewStock.editerStock, name='editerStock'),
    path('stock/total/editer/supprimer/<pk>/', viewStock.deleteStock, name='deleteStock'),

    path('stock/alloue/', viewStock.listStock, name='listStockAlloue'),
    path('stock/alloue/get/<pk>/', viewStock.getStock, name='getStockAlloue'),
    path('stock/alloue/editer/<pk>/', viewStock.editerStock, name='editerStockAlloue'),
    path('stock/alloue/supprimer/<pk>/', viewStock.deleteStock, name='deleteStockAlloue'),

    # Gestion des taches
    path('tache/liste/', viewTache.listTache, name='listTache'),
    path('tache/get/<id>/', viewTache.getTache, name='getTache'),
    path('tache/calendrier/', viewTache.listTache, name='listTacheCal'),
    path('tache/liste/supprimer/<id>', viewTache.deleteTache, name='deleteTache'),
    path('tache/liste/editer/<id>', viewTache.editerTache, name='editerTache'),
    path('tache/ajouter/', viewTache.ajouterTache, name='ajouterTache'),

    #Gestion des affectations
    path('affecter/supprimer/<pk>/', viewAffecter.supprimer, name='supprimerAffectation'),

    # url(r'api/', include(router.urls))

    # Gestion des triathlon
    path('triathlon/select/<id>/', viewTriathlon.selectTriathlon, name='selectTriathlon'),
    path('triathlon/choisirTriathlon/', viewTriathlon.choisirTriathlon, name='choisirTriathlon'),
    path('triathlon/ajouterTriathlon/', viewTriathlon.ajouterTriathlon, name='ajouterTriathlon'),
    path('triathlon/voirTriathlon/<pk>/', viewTriathlon.voirTriathlon, name='voirTriathlon'),
    path('triathlon/supprimer/<pk>/', viewTriathlon.supprimerTriathlon, name='supprimerTriathlon'),
    path('triathlon/editer/<pk>/', viewTriathlon.editerTriathlon, name='editerTriathlon'),

    #dashboard
    path('personnel/donation/triathlon_courant', viewSponsorDonation.listDonationTriathlon, name='listDonationTriathlon'),
    path('personnel/benevole/affecter/', viewBenevole.listBenevoleAffecter, name='listBenevoleAffecter'),
    path('tache/list/retard', viewTache.listTacheRetard, name='listTacheRetard'),

]
