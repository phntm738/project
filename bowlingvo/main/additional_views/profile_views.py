from ..models import FinishedLesson, FinishedSection, FinishedLanguage, UserProfile
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import *
from django.core.validators import EmailValidator
from .authorization_views import send_mail
from django.contrib.auth import logout


@require_GET
@login_required(login_url='/main/login')
def get_profile(request):
    template_name = 'main/profile.html'
    user = request.user
    profile = UserProfile.objects.get(user=user)
    finished = [len(list(FinishedLesson.objects.filter(user=user))),
                len(list(FinishedSection.objects.filter(user=user))),
                len(list(FinishedLanguage.objects.filter(user=user)))]
    last_lessons = [fl.lesson for fl in FinishedLesson.objects.filter(user=user).order_by('-date')][:5]
    return render(request, template_name,
                  {'profile': profile, 'is_profile': True, 'last_lessons': last_lessons, 'finished': finished})


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'main/edit_profile.html'

    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return render(request, self.template_name, {'profile': profile})

    def post(self, request):
        profile = UserProfile.objects.get(user=request.user)
        errors = {'username': [], 'email': [], 'old_password': [], 'new_password1': [], 'new_password2': []}
        success = []
        username = request.POST.get('username')
        if username:
            try:
                u = User.objects.get(username=username)
                errors['username'].append('Это имя пользователя занято')
            except User.DoesNotExist:
                request.user.username = username
                request.user.save()
                success.append('Имя пользователя успешно изменено')
        email = request.POST.get('email')
        if email:
            validator = EmailValidator()
            try:
                validator(email)
                request.user.email = email
                request.user.save()
                send_mail(request, request.user, 'Изменение почтового адреся для BowLingvo')
                u = User.objects.get(email=email)
                u.is_active = False
                u.save()
                return render(request, 'main/email_changed.html', {'email': email})
            except ValidationError:
                errors['email'].append('Некорректный email')
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        if old_password or new_password1 or new_password2:
            user = authenticate(username=request.user.username, password=old_password)
            if user is not None:
                validators = [MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator, UserAttributeSimilarityValidator]
                for val in validators:
                    validator = val()
                    try:
                        validator.validate(new_password1, user=request.user)
                    except ValidationError as exception:
                        errors['new_password1'].append(exception)
                if not errors['new_password1']:
                    if new_password1 == new_password2:
                        request.user.set_password(new_password1)
                        request.user.save()
                        success.append('Пароль успешно изменен')
                    else:
                        errors['new_password2'].append('Пароли не совпадают')
            else:
                errors['old_password'].append('Неверный пароль')
        return render(request, self.template_name,
                      {'profile': profile, 'errors': errors, 'success': success})

