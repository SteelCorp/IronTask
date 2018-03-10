from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from irontask_app.models import T


def listTriathlon(request):
    return 0