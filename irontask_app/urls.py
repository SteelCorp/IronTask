from django.contrib import admin
from django.urls import path
from irontask_app.views import viewSponsor



urlpatterns = [
    path('listSponsor/', viewSponsor.listSponsor),
    path('getSponsor/<siret>/', viewSponsor.getSponsor, name='getSponsor')

]