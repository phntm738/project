import pprint
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.


def index(request):
    colors = {
        "yellow": 'amarillo',
        "green": 'verde',
        "blue": 'azul',
        "red": 'rojo'
    }
    return render(request, 'main/my_form.html', {'username': 'USERNAME', 'colors': colors})


def results(request):
    html = '<html><body>'
    html += pprint.pformat(dict(request.POST.lists()))
    html += '</body></html>'
    return HttpResponse(html)