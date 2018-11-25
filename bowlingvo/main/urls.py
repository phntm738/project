from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('results', views.results),
    path('login', views.login),
    path('do-login', views.do_login),
]