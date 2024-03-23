from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    about_link = '<a href="/rango/about/">About</a>'
    return HttpResponse(f"<h1>Rango says hey there partner!</h1><p>Go to the {about_link}</p>")


def about(request):
    about_link = '<a href="/rango/">Index</a>.'
    return HttpResponse(f"<h1>Rango says here is the about page.</h1><p>Go to the {about_link}</p>")
