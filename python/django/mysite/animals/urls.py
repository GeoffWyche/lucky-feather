from django.conf.urls import patterns, url
from animals import views

urlpatterns = patterns('',
#                       url(r'^$', views.guess, name='guess'),
                       url(r'^(\d+)$', views.guess),
                       )
