from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from irontask_app.decorators import triathlon_required


@login_required(login_url='login/')
@triathlon_required
def index(request):
    return render(request, 'index.html')
