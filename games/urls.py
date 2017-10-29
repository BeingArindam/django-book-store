from django.conf.urls import url
from . import views

app_name = 'games'

urlpatterns = [
    #/games/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /games/51
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    url(r'add/$', views.GameCreate.as_view(), name='game-create'),
    url(r'(?P<pk>[0-9]+)/edit/$', views.GameUpdate.as_view(), name='game-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.GameDelete.as_view(), name='game-delete'),


]
