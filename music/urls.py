from django.conf.urls import url
from . import views
# Must be done!
app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/albumId/
    url(r'^(?P<albumId>[0-9]*)[/]?$', views.details, name='details'),

    # /music/albumId/loveIt
    url(r'^(?P<albumId>[0-9]*)/loveIt[/]?$', views.loveIt, name='loveIt'),


]
