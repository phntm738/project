from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .additional.task_gen import lex_task_gen


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
    )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email',
                             required=True,
                             help_text="Enter a valid email.",
                             )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Registration_view(View):
    form_class = RegistrationForm
    template_name = 'main/registration_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('/main/login')
        else:
            return render(request, self.template_name, {'form': form})


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
