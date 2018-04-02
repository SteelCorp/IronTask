from django.contrib import admin
from django.urls import path, include
from irontask_app.views import viewSponsor, viewIndex, viewLogin, viewIntervenant, viewBenevole
from django.conf.urls import url, include

from irontask_app import api
from irontask_app import views

urlpatterns = [

    # Gestion de la session
    url('login/', viewLogin.user_login),
    url('logout/', viewLogin.logout_user, name='logout_user'),
    path('', viewIndex.index, name='index'),

    # Gestion des sponsors
    path('sponsor/', viewSponsor.listSponsor, name='listSponsor'),
    path('sponsor/get/<siret>/', viewSponsor.getSponsor, name='getSponsor'),
    path('sponsor/editer/<siret>/', viewSponsor.editerSponsor, name='editerSponsor'),
    path('sponsor/supprimer/<siret>/', viewSponsor.deleteSponsor, name='deleteSponsor'),

    # Gestion des intervenants
    path('intervenant/', viewIntervenant.listIntervenant, name='listIntervenant'),
    path('intervenant/get/<pk>/', viewIntervenant.getIntervenant, name='getIntervenant'),
    path('intervenant/editer/<pk>/', viewIntervenant.editerIntervenant, name='editerIntervenant'),
    path('intervenant/supprimer/<pk>/', viewIntervenant.deleteIntervenant, name='deleteIntervenant'),

    # Gestion des benevoles
    path('benevole/', viewBenevole.listBenevole, name='listBenevole'),
    path('benevole/get/<pk>/', viewBenevole.getBenevole, name='getBenevole'),
    path('benevole/editer/<pk>/', viewBenevole.editerBenevole, name='editerBenevole'),
    path('benevole/supprimer/<pk>/', viewBenevole.deleteBenevole, name='deleteBenevole'),

    # url(r'api/', include(router.urls))
]
