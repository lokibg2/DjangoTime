from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse('<h1> Hey Buddy! :) </h1>')


def error(request):
    return HttpResponse('Error! Wrong Page!!')

