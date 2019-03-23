from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .additional.task_gen import task_gen
from django.http import Http404

from .my_views.authorization_views import *
from .my_views.education_views import *


@method_decorator(login_required, name='get')
class ProfileView(View):
    template_name = 'main/profile.html'

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        finished_lessons = FinishedLesson.objects.all().filter(user_id=user.id)
        return render(request, self.template_name, {'profile': profile, 'is_profile': True, 'last_lessons': finished_lessons})


def stop(request):
    raise Http404


from types import SimpleNamespace as SN

import os
@login_required(login_url='/main/login')
def test(request):
    profile = UserProfile.objects.get(pk=1)
    l = Language.objects.get(pk=1)
    s = Section.objects.get(name='Еда')
    les = Lesson.objects.get(pk=4)
    theory = [
        {'for_sing': 'apple',
         'for_plur': 'apples',
         'rus_sing': 'яблоко',
         'rus_plur': 'яблоки'},
        {'for_sing': 'banana',
         'for_plur': 'bananas',
         'rus_sing': 'банан',
         'rus_plur': 'бананы'},
        {'for_sing': 'orange',
         'for_plur': 'oranges',
         'rus_sing': 'апельсин',
         'rus_plur': 'апельсины'},
        {'for_sing': 'pear',
         'for_plur': 'pears',
         'rus_sing': 'груша',
         'rus_plur': 'груши'},
        {'for_sing': 'blum',
         'for_plur': 'blums',
         'rus_sing': 'слива',
         'rus_plur': 'сливы'}
    ]

    theory = [
        SN(for_sing='pear', for_plur='pears', rus_sing='груша', rus_plur='груши'),
        SN(for_sing='pear', for_plur='pears', rus_sing='груша', rus_plur='груши')
    ]

    tasks = [
        {'type': 'choice',
         'text': 'banana',
         'answer': 'банан',
         'choices': ['яблоко', 'банан', 'слива', 'апельсин']},
        {'type': 'input',
         'text': 'Зеленое яблоко лежало на столе\nThere was a green _____ on the table',
         'answer': 'apple'
        }
    ]

    return render(request, 'main/lesson_page.html', {'profile': profile, 'theory': theory, 'tasks': tasks, 'language': l, 'section': s, 'lesson': les})
    return render(request, 'main/test.html', {'page_name': 'test', 'script': True})
