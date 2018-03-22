from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from irontask_app.forms.LoginForm import ConnexionForm

from irontask_app.models import UserProfile


def user_login(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                print(form.errors)

    form = ConnexionForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='login/')
def logout_user(request):
    logout(request)

    return HttpResponseRedirect('/login/')
