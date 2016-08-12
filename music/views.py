from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Album


def index(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'music/index.html', context)


def error(request):
    return HttpResponse('<h1 style="text-align:center">Error! Wrong Page!!</h1>')


def details(request, albumId):
    return HttpResponse('<h2 style="text-align:center"> You\'re at Album No : ' + albumId + '</h2>')
