from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('results', views.results),
    path('login', views.send_login_form),
    path('do-login', views.do_login),
    path('do-logout', views.do_logout),
    path('register', views.send_register_form),
    path('do-register', views.do_register)
]