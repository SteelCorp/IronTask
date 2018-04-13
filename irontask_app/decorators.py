from irontask_app.views import viewLogin
from django.shortcuts import render, redirect
from irontask_app.views.viewTriathlon import choisirTriathlon

def triathlon_required(f):
    def wrap(request, *args, **kwargs):
        if 'idTriathlon' not in request.session:
            return redirect(choisirTriathlon)
        else:
            return f(request, *args, **kwargs)
    return wrap