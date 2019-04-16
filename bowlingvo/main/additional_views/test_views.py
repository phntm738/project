from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token as get_csrf
from django.contrib.auth.password_validation import *


def test(request):
    if request.method == 'GET':
        return render(request, 'main/test.html', {'user': request.user})
    if request.method == 'POST':
        a = request.POST.get('test')
        return HttpResponse(str(type(a)))
        password = '1234567'
'''    validator = MinimumLengthValidator()
    try:
        validator.validate(password)
    except ValidationError as exception:
        return HttpResponse(exception)
    return HttpResponse(1) '''
