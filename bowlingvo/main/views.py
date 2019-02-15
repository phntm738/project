from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .additional.task_gen import lex_task_gen
from django.http import Http404

from .my_views.authorization_views import *
from .my_views.education_views import *


#@method_decorator(login_required, name='get')
class ProfileView(View):
    template_name = 'main/profile.html'

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        finished_lessons = FinishedLesson.objects.all().filter(user_id=user.id)
        return render(request, self.template_name, {'profile': profile, 'is_profile': True, 'last_lessons': finished_lessons})


@login_required(login_url='/main/login')
def get_sections(request, language_name):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    language = Language.objects.get(url_name=language_name)
    sections = Section.objects.all().filter(language_id=language.id)
    return render(request, 'main/language_page.html',
                  {'profile': profile, 'page_name': language.name, 'language': language, 'sections': sections})


def stop(request):
    raise Http404


import os
def test(request):
    if not request.user.is_authenticated:
        return redirect('/main/login')
    return render(request, 'main/test.html', {'page_name': 'test', 'script': True})
