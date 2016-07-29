import requests
from django.http import HttpResponse
from django.shortcuts import render
from cakesapi.models import Cake


from .helpers import run


def home(request):
    cake = Cake.objects.all()
    return render(request, "cake.html", {'cake': cake})


def save(request):
    run()

