from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def index(request):
    return render(request,'default_app/index.html')


def gallery(request):
    return render(request,'default_app/gallery.html')


def terms(request):
    return render(request,'default_app/tc.html')


def privacy(request):
    return render(request,'default_app/pp.html')