from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# each function renders the content for the views


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def details(request, albumId):
    album = {'album' : get_object_or_404(Album, pk=albumId)}
    return render(request, 'music/details.html', album)


def loveIt(request, albumId):
    album = get_object_or_404(Album, pk=albumId)
    try:
        # modify love option
        song = album.song_set.get(id=request.POST['song'])
        song.isFavorite = not song.isFavorite
        song.save()
        # redirect
        return render(request, 'music/details.html', {'album': album})

    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {'album': album, 'error_message': "Invalid Song"})
