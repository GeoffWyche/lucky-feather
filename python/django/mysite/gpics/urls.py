from django.conf.urls import patterns, url
from gpics import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                   )