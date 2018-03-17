from django.contrib import admin
from django.urls import path, include
from irontask_app.views import viewSponsor, viewIndex, viewLogin
from django.conf.urls import url, include

from irontask_app import api
from irontask_app import views

urlpatterns = [
    url('login/', viewLogin.user_login),
    url('logout/', viewLogin.logout_user,  name='logout_user'),
    path('', viewIndex.index, name='index'),
    path('sponsor/', viewSponsor.listSponsor, name='listSponsor'),
    path('sponsor/get/<siret>/', viewSponsor.getSponsor, name='getSponsor'),
    path('sponsor/editer/<siret>/', viewSponsor.editerSponsor, name='editerSponsor'),

    # url(r'api/', include(router.urls))
]
