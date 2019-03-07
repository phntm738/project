from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect
from ..models import *
from ..additional.task_gen import task_gen
from datetime import datetime


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
    fsections = FinishedSection.objects.filter(user=user)
    a = []
    for fs in fsections:
        a.append(fs.section)
    fsections = a
    all_lex_sections = sections.filter(sec_type='L')
    lex_sections = []
    for sec in all_lex_sections:
        lex_sections.append([sec, 'finished' if sec in fsections else 'active'])
    all_gram_sections = sections.filter(sec_type='G')
    gram_sections = []
    for sec in all_gram_sections:
        gram_sections.append([sec, 'active' if sec in fsections else 'locked'])
    for section in gram_sections:
        if section[1] == 'locked':
            section[1] = 'active'
            break
        elif section[1] == 'active':
            section[1] = 'finished'

    return render(request, 'main/language_page.html',
                 {'profile': profile, 'language': language, 'lex_sections': lex_sections, 'gram_sections': gram_sections})


@require_GET
@login_required(login_url='/main/login')
def section_page(request, language_name, section_name):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    language = Language.objects.get(url_name=language_name)
    section = Section.objects.filter(language_id=language.id).get(url_name=section_name)
    lessons = Lesson.objects.filter(section_id=section.id)
    lessons = lessons.order_by('order')
    flessons = FinishedLesson.objects.filter(user_id=user.id)
    finished_lessons = [f.lesson for f in flessons]
    all_lessons = []
    for lesson in lessons:
        all_lessons.append([lesson, 'active' if lesson in finished_lessons else 'locked'])
    for lesson in all_lessons:
        if lesson[1] == 'locked':
            lesson[1] = 'active'
            break
        elif lesson[1] == 'active':
            lesson[1] = 'finished'
    return render(request, 'main/section_page.html',
                  {'profile': profile, 'language': language, 'section': section, 'lessons':all_lessons})


def finished_section_check(user, section):
    all_lessons = Lesson.objects.filter(section=section)
    flessons = FinishedLesson.objects.filter(user=user)
    a = []
    for lesson in all_lessons:
        a.append(lesson)
    all_lessons = a
    for fl in flessons:
        try:
            all_lessons.remove(fl.lesson)
        except ValueError:
            pass
    if len(a) > 0:
        try:
            fs = FinishedSection.objects.get(user=user, section=section)
            fs.delete()
        except FinishedSection.DoesNotExist:
            pass
    else:
        try:
            fs = FinishedSection.objects.get(user=user, section=section)
        except FinishedSection.DoesNotExist:
            fs = FinishedSection(user=user, section=section)
            fs.save()


@login_required(login_url='/main/login')
def lesson_page(request, language_name, section_name, lesson_order):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    language = Language.objects.get(url_name=language_name)
    section = Section.objects.filter(language_id=language.id).get(url_name=section_name)
    lesson = Lesson.objects.filter(section_id=section.id).get(order=lesson_order)

    if request.method == 'GET':
        tasks = task_gen(lesson.id)
        return render(request, 'main/lesson_page.html',
                      {'profile': profile, 'language': language, 'section': section, 'lesson_name': str(lesson), 'lesson': lesson, 'tasks': tasks})

    if request.method == 'POST':
        score = int(request.POST.get('score'))
        try:
            fl = FinishedLesson.objects.get(user=user, lesson=lesson)
            date1 = datetime.now()
            date2 = fl.date
            if (date1 - date2).days >= 1:
                profile.score += score
            fl.save()
        except FinishedLesson.DoesNotExist:
            fl = FinishedLesson(user=user, lesson=lesson)
            fl.save()
            profile.score += score
        finished_section_check(user, section)
        profile.save()
#        finished_section_check(user, section)
        return redirect('section', language_name=language.url_name, section_name=section.url_name)
