from django.contrib.auth.decorators import login_required
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
    sections = Section.objects.all().filter(language_id=language.id)
    return render(request, 'main/language_page.html',
                 {'profile': profile, 'language': language, 'sections': sections})

