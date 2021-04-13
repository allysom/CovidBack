from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Exame


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def cadastro(request):
    template = loader.get_template('cadastro.html')
    return HttpResponse(template.render({}, request))


def index(request):
    exames = Exame.objects.all()
    print(exames)
    template = loader.get_template('exames.html')
    context = {
        'exames': exames,
    }
    return HttpResponse(template.render(context, request))


def detail(request, exame_id):
    return HttpResponse("Estou vendo o exame de ID: " + str(exame_id))


def exame_add(request):
    template = loader.get_template('exames-add.html')
    return HttpResponse(template.render({}, request))


def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render({}, request))