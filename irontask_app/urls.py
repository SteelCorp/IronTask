from django.contrib import admin
from django.urls import path, include
from irontask_app.views import viewSponsor
from django.conf.urls import url, include
from rest_framework import routers
from irontask_app import api
from irontask_app import views

"""router = routers.DefaultRouter()

router.register(r'sponsor', api.SponsorViewSet)"""



urlpatterns = [
    path('listSponsor/', viewSponsor.listSponsor, name='listSponsor'),
    path('getSponsor/<siret>/', viewSponsor.getSponsor, name='getSponsor'),
    path('editerSponsor/<siret>/', viewSponsor.editerSponsor, name='editerSponsor'),

    #url(r'api/', include(router.urls))
]

