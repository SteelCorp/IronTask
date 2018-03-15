from django.contrib import admin
from django.urls import path, include
from irontask_app.views import viewSponsor, viewIndex
from django.conf.urls import url, include

from irontask_app import api
from irontask_app import views





urlpatterns = [
    path('', viewIndex.index, name='index'),
    path('sponsor/', viewSponsor.listSponsor, name='listSponsor'),
    path('sponsor/get/<siret>/', viewSponsor.getSponsor, name='getSponsor'),
    path('sponsor/editer/<siret>/', viewSponsor.editerSponsor, name='editerSponsor'),

    #url(r'api/', include(router.urls))
]

