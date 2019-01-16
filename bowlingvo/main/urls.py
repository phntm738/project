from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login', auth_views.LoginView.as_view(template_name='main/login_form2.html')),
    path('do-logout', auth_views.LogoutView.as_view()),
    path('register', views.Registration_view.as_view()),
    path('test', views.test),
    path('<str:language_name>', views.get_sections),
]