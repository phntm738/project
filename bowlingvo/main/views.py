from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .additional.task_gen import task_gen
from django.http import Http404

from .additional_views.authorization_views import *
from .additional_views.education_views import *
from .additional_views.game_views import *


def handler404(request, exception):
    return HttpResponse(1)


@method_decorator(login_required, name='get')
class ProfileView(View):
    template_name = 'main/profile.html'

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        finished_lessons = list(FinishedLesson.objects.all().filter(user_id=user.id).order_by('-date'))
        for i in range(len(finished_lessons)):
            fl = finished_lessons[i]
            finished_lessons[i] = fl.lesson
        return render(request, self.template_name, {'profile': profile, 'is_profile': True, 'last_lessons': finished_lessons})


def stop(request):
    raise Http404


from django.middleware.csrf import get_token as get_csrf


def test(request):
    if request.method == 'GET':
        response = render(request, 'main/test.html')
        csrf = get_csrf(request)
        response.set_cookie('csrftoken', csrf)
        return response
    if request.method == 'POST':
        inp = request.POST.get('test')
        return HttpResponse(inp)