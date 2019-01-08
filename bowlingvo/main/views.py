from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import auth
from .my_views.session_views import *
from .models import *


def index(request):
    if not request.user.is_authenticated:
        request.session['error_message'] = 'Please, login'
        return redirect('/main/login')
    languages = Language.objects.all()
    return render(request, 'main/index.html',
                  {'authorized': True, 'username': request.user.username, 'page_name': 'index', 'languages': languages})


def get_sections(request, language_name):
    if not request.user.is_authenticated:
        request.session['error_message'] = 'Please, login'
        return redirect('/main/login')
    language = Language.objects.get(url_name=language_name)
    sections = Section.objects.all().filter(language_id=language.id)
    return render(request, 'main/language_page.html',
                  {'authorized': True, 'username': request.user.username, 'page_name': language.name, 'language': language, 'sections': sections})


def test(request):
    if not request.user.is_authenticated:
        return redirect('/main/login')
    return render(request, 'main/test.html', {'authorized': True, 'username': request.user.username, 'page_name': 'test', 'script': True})
