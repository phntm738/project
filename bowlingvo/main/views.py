import pprint
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import auth


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        request.session['error_message'] = 'Please, login'
        return redirect('/main/login')
    colors = {
        "yellow": 'amarillo',
        "green": 'verde',
        "blue": 'azul',
        "red": 'rojo'
    }
    return render(request, 'main/my_form.html', {'username': request.user.username, 'colors': colors})


def results(request):
    html = '<html><body>'
    html += pprint.pformat(dict(request.POST.lists()))
    html += '</body></html>'
    return HttpResponse(html)


def login(request):
    error_message = request.session.get('error_message', '')
    return render(request,'main/login_form.html', {'error_message': error_message})


def do_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        request.session['error_message'] = ''
        return redirect('/main/')
    request.session['error_message'] = 'wrong login or password'
    return redirect('/main/login')