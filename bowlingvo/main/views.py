from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django import forms
from django.views import View
from django.contrib import auth
from .models import *
from .additional.task_gen import lex_task_gen


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150, required=True)
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Pasword', max_length=30, required=True)
    password2 = forms.CharField(label='Password again', max_length=30, required=True)


class Registration_view(View):
    form_class = RegistrationForm
    template_name = 'main/registration_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass


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
    return HttpResponse(lex_task_gen(1))
    return render(request, 'main/test.html', {'authorized': True, 'username': request.user.username, 'page_name': 'test', 'script': True})
