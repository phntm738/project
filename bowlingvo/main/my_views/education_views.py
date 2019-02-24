from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from ..models import *


@require_GET
@login_required(login_url='/main/login')
def index(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    languages = Language.objects.all()
    return render(request, 'main/index.html',
                  {'profile': profile, 'languages': languages})


@require_GET
@login_required(login_url='/main/login')
def language_page(request, language_name):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    language = Language.objects.get(url_name=language_name)
    sections = Section.objects.filter(language_id=language.id)
    lex_sections = sections.filter(sec_type='L')
    gram_sections = sections.filter(sec_type='G')
    return render(request, 'main/language_page.html',
                 {'profile': profile, 'language': language, 'lex_sections': lex_sections, 'gram_sections': gram_sections})


@require_GET
@login_required(login_url='/main/login')
def section_page(request, language_name, section_name):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    section = Section.objects.get(url_name=section_name)
    lessons = Lesson.objects.filter(section_id=section.id)
    lessons = lessons.order_by('order')
    flessons = FinishedLesson.objects.filter(user_id=user.id)
    finished_lessons = [f.lesson for f in flessons]
    all_lessons = []
    for lesson in lessons:
        all_lessons.append([str(lesson), lesson in finished_lessons])
    for lesson in all_lessons:
        if lesson[1] == False:
            lesson[1] = True
            break
    return render(request, 'main/section_page.html',
                  {'profile': profile, 'section': section, 'lessons':all_lessons})

