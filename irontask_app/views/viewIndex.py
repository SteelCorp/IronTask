from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def index (request):

    return render(request, 'index.html')