from django.shortcuts import render

def viewtest(request):
    return render(request, 'index.html')