from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^$', views.index),
    url('results', views.results)
]