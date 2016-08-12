from django.http import HttpResponse, Http404
from .models import Album

def index(request):
    albums = Album.objects.all()

    html = '<h1 style="text-align:center"> This is Music!!!! :) </h1>'
    html += '<hr><br><ul>'

    for album in albums:
        url = '/music/' + str(album.id)
        html += '<li><a href = "' + url + '">' + album.albumTitle + '</a>'
    return HttpResponse(html)


def error(request):
    return HttpResponse('<h1 style="text-align:center">Error! Wrong Page!!</h1>')


def details(request, albumId):
    return HttpResponse('<h2 style="text-align:center"> You\'re at Album No : ' + albumId + '</h2>')
