from .additional_views.authorization_views import *
from .additional_views.profile_views import *
from .additional_views.education_views import *
from .additional_views.game_views import *
from .additional_views.error_views import *
from .additional_views.test_views import *
from django.shortcuts import render


def sorry(request):
    return render(request, 'main/sorry.html')
