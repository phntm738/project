from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import models as auth_models


def send_login_form(request):
    error_message = request.session.get('error_message', '')
    return render(request,'main/login_form.html', {'error_message': error_message, 'page_name': 'Login'})


def do_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['error_message'] = ''
        return redirect('/main/')
    request.session['error_message'] = 'wrong login or password'
    return redirect('/main/login')


def do_logout(request):
    logout(request)
    return redirect('/main/login')


def send_register_form(request):
    error_message = request.session.get('error_message', '')
    return render(request, 'main/register_form.html', {'error_message': error_message, 'page_name': 'Register'})


def do_register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password_again = request.POST['password_again']
    if password != password_again:
        request.session['error_message'] = "passwords don't match"
        redirect('/main/register')
