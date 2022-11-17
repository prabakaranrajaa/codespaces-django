"""django doc"""
#from django.http import HttpRequest
from django.shortcuts import render


def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Prabakaranraja Portfolio",
        },
    )
def mysite(request):
    return render(
        request,
        "my.html",
        {
            "title": "Prabakaranraja",
        },
    )

def contact(request):
    return render(
        request,
        "contactme.html",
        {
            "title": "Prabakaranraja",
        },
    )

def hobbies(request):
    return render(
        request,
        "hobbies.html",
        {
            "title": "Prabakaranraja",
        },
    )

def songs(request):
    return render(
        request,
        "songs.html",
        {
            "title": "Prabakaranraja",
        },
    )
def pics(request):
    return render(
        request,
        "pics.html",
        {
            "title": "Prabakaranraja",
        },
    )