from django.conf.urls import url
from .import views


urlpatterns = [
    #/music/
    url(r'^$',views.index,name='index'),
    #/music/121/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
    #/music/id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
]
