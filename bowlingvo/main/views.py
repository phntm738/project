from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .additional.task_gen import lex_task_gen

from .my_views.authorization_views import *


class Profile_view(View):
    template_name = 'main/profile.html'

    def get(self, request):
        user = request.user
        profile = User_Profile.objects.get(user=user)
        finished_lessons = Finished_Lesson.objects.all().filter(user_id=user.id)
        return render(request, self.template_name, {'profile': profile, 'is_profile': True, 'last_lessons': finished_lessons})


def index(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/main/login')
    profile = User_Profile.objects.get(user=user)
    languages = Language.objects.all()
    return render(request, 'main/index.html',
                  {'profile': profile, 'page_name': 'index', 'languages': languages})


def get_sections(request, language_name):
    if not request.user.is_authenticated:
        request.session['error_message'] = 'Please, login'
        return redirect('/main/login')
    user = request.user
    profile = User_Profile.objects.get(user=user)
    language = Language.objects.get(url_name=language_name)
    sections = Section.objects.all().filter(language_id=language.id)
    return render(request, 'main/language_page.html',
                  {'profile': profile, 'page_name': language.name, 'language': language, 'sections': sections})


def test(request):
    if not request.user.is_authenticated:
        return redirect('/main/login')
    return render(request, 'main/test.html', {'page_name': 'test', 'script': True})
