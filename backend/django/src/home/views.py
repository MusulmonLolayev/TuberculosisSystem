from django.shortcuts import render

def index(request):
    return render(request, 'home/base.html')

def spa(request):
    return render(request, 'spa/index.html')