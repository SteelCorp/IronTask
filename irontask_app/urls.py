from django.contrib import admin
from django.urls import path
from irontask_app.views import viewtest


urlpatterns = [
    path('', viewtest.viewtest)
]