from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Album


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def error(request):
    return HttpResponse('<h1 style="text-align:center">Error! Wrong Page!!</h1>')


def details(request, albumId):
    try:
        album = {'album' : Album.objects.get(pk=albumId)}
    except Album.DoesNotExist:
        raise Http404('Oh no! That one has escaped somehow! -_-');
    return render(request, 'music/details.html', album  )

