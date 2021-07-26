from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse("Rango says hey there partner! go to about: <a href = 'http://127.0.0.1:8000/rango/about' > about </a>")

def about (request):
    return HttpResponse("Rango says this is the about page <a href= 'http://127.0.0.1:8000/rango' > back </a> ")
