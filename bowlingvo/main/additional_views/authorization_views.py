from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.views import View
from ..models import *
from ..forms import *

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


NEED_EMAIL = True


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)


account_activation_token = TokenGenerator()


class RegistrationView(View):
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
            profile = UserProfile()
            profile.user = user
            profile.save()

            if NEED_EMAIL:
                send_mail(request, user)
                return render(request, 'main/email_conf.html', {'email': user.email})
            else:
                user.is_active = True
                user.save()
                login(request, user)
                return redirect('/main')
        else:
            return render(request, self.template_name, {'form': form})


def send_mail(request, user, mail_subject=None, template=None):
    current_site = get_current_site(request)
    basic_mail_subject = 'Активация аккаунта на BowLingvo'
    mail_subject = mail_subject or basic_mail_subject
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    template = template or 'main/acc_activation.html'
    message = render_to_string(template, {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token,
    })
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.send()


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/main')
    else:
        return HttpResponse('Activation link is invalid!')
