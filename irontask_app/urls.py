from django.contrib import admin
from django.urls import path, include
from irontask_app.views import viewSponsor, viewIndex, viewLogin, \
    viewIntervenant, viewBenevole, viewStock, viewTriathlon, viewTache
from django.conf.urls import url, include

from irontask_app import api
from irontask_app import views

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
    path('personnel/donation/get/<id>/', viewSponsor.getSponsor, name='getDonation'),
    path('personnel/donation/editer/<id>/', viewSponsor.editerSponsor, name='editerDonation'),
    path('personnel/donation/supprimer/<id>/', viewSponsor.deleteDonation, name='deleteDonation'),

    # Gestion des intervenants
    path('personnel/intervenant/', viewIntervenant.listIntervenant, name='listIntervenant'),
    path('personnel/intervenant/get/<siret>/', viewIntervenant.getIntervenant, name='getIntervenant'),
    path('personnel/intervenant/supprimer/<siret>/', viewIntervenant.deleteIntervenant, name='deleteIntervenant'),

    # Gestion des benevoles
    path('personnel/benevole/', viewBenevole.listBenevole, name='listBenevole'),
    path('personnel/benevole/get/<pk>/', viewBenevole.getBenevole, name='getBenevole'),
    path('personnel/benevole/editer/<pk>/', viewBenevole.editerBenevole, name='editerBenevole'),
    path('personnel/benevole/supprimer/<pk>/', viewBenevole.deleteBenevole, name='deleteBenevole'),

    # Gestion des stocks
    path('stocks/', viewStock.listStock, name='listStock'),
    path('stocks/get/<pk>/', viewStock.getStock, name='getStock'),
    path('stocks/editer/<pk>/', viewStock.editerStock, name='editerStock'),
    path('stocks/supprimer/<pk>/', viewStock.deleteStock, name='deleteStock'),

    # Gestion des taches
    path('tache/', viewTache.listTache, name='listTache' ),

    # url(r'api/', include(router.urls))

    # Gestion des triathlon
    path('triathlon/select/<id>/', viewTriathlon.selectTriathlon, name='selectTriathlon'),
    path('triathlon/choisirTriathlon/', viewTriathlon.choisirTriathlon, name='choisirTriathlon'),
    path('triathlon/ajouterTriathlon/', viewTriathlon.ajouterTriathlon, name='ajouterTriathlon'),



]
