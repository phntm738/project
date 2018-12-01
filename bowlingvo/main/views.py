from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import auth
from .my_views.session_views import *



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
    return render(request, 'main/my_form.html', {'username': request.user.username, 'colors': colors, 'page_name': 'index'})


def test(request):
    return render(request, 'main/test.html')
