from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token as get_csrf
from django.contrib.auth.password_validation import *
from ..models import *


def test(request):
    f = open('log.txt', 'w')
    for key in Key2Lesson.objects.filter(key__startswith='w'):
        words = list(Word.objects.filter(key=key.key))
        if len(words) != 2:
            f.write(str(key.key)+'\n')
    f.close()
    return HttpResponse(1)
