from django.conf.urls import url
from . import views


urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/id/
    url(r'^(?P<albumId>[0-9]*)[/]?$', views.details, name='details'),

    # Invalid
    url(r'.*', views.error, name='error')

]
