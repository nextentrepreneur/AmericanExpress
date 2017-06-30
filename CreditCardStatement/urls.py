from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^profile/(?P<ID>[a-zA-Z0-9]+)$', views.profile, name='profile'),
	url(r'^profile/$', views.profile, name='profile')
]