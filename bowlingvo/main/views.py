from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .additional.task_gen import task_gen
from .additional.content.english import main
from django.http import Http404

from .my_views.authorization_views import *
from .my_views.education_views import *


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


def test1(request):
    if request.method == 'GET':
        ans = '<a href="#">aaa</a>'
        return HttpResponse(ans)
    if request.method == 'POST':
        score = request.POST.get('score')
        return HttpResponse(score)


def test(request):
    main()
    return render(request, 'main/test.html', {})
    return render(request, 'main/test.html', {'page_name': 'test', 'script': True})
