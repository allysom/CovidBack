from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .models import Exame
from login.models import Usuario


def login(request):
    if request.method == 'GET':
        template = loader.get_template('login.html')
        return HttpResponse(template.render({}, request))

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        user = authenticate(request, username=email, password=senha)
        if user is not None:
            auth_login(request, user)
            menu_template = loader.get_template('menu.html')
            return HttpResponse(menu_template.render({}, request))

        else:
            template = loader.get_template('login.html')
            return HttpResponse(template.render({}, request))
            

def cadastro(request):
    if request.method == "GET":
        template = loader.get_template('cadastro.html')
        return HttpResponse(template.render({}, request))

    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']

        usuario = Usuario(
            username=email,
            email=email,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            endereco=endereco
        )

        usuario.save()
        usuario.set_password(senha)
        usuario.save()

        login_template = loader.get_template('login.html')
        return HttpResponse(login_template.render({}, request))


def index(request):
    if request.user.is_authenticated:
        exames = Exame.objects.filter(user=request.user)
        template = loader.get_template('exames.html')
        context = {
            'exames': exames,
        }
        return HttpResponse(template.render(context, request))
    else:
        login_template = loader.get_template('login.html')
        return HttpResponse(login_template.render({}, request)) 




def detail(request, exame_id):
    if request.user.is_authenticated:
        try:
            exame = Exame.objects.get(id=exame_id)
        except Exception as e:
            print(e)
            exame = None
        
        if exame:
            context = {
                "exame": exame
            }
            template = loader.get_template('exame.html')
            return HttpResponse(template.render(context, request))

        else:
            exames = Exame.objects.filter(user=request.user)
            context = {
                "exames": exames
            }
            exames_template = loader.get_template('exames.html')
            return HttpResponse(exames_template.render(context, request)) 
    else:
        login_template = loader.get_template('login.html')
        return HttpResponse(login_template.render({}, request)) 


def calcula_resultado(exame):
    resultado = 0.0

    if exame.febre:
        resultado = resultado + 4.0
    if exame.tosse: 
        resultado = resultado + 4.0
    if exame.cansaco:
        resultado = resultado + 4.0
    if exame.desconforto:
        resultado = resultado + 4.0
    if exame.dor_garganta:
        resultado = resultado + 4.0
    if exame.diarreia:
        resultado = resultado + 4.0
    if exame.conjuntivite:
        resultado = resultado + 4.0
    if exame.dor_cabeca:
        resultado = resultado + 4.0
    if exame.perda_paladar:
        resultado = resultado + 4.0
    if exame.erupcao_cutanea:
        resultado = resultado + 4.0
    # Sintomas Graves 60% de chance
    if exame.falta_ar:
        resultado = resultado + 20.0
    if exame.dor_peito:
        resultado = resultado + 20.0
    if exame.perda_fala:
        resultado = resultado + 20.0

    exame.resultado = resultado
    exame.save()

def exame_add(request):
    if request.user.is_authenticated:
        
        if request.method == "GET":
            template = loader.get_template('exames-add.html')
            return HttpResponse(template.render({}, request))
        
        if request.method == "POST":

            febre = True if 'febre' in request.POST and request.POST['febre'] == 'true' else False
            tosse = True if 'tosse' in request.POST and request.POST['tosse'] == 'true' else False
            cansaco = True if 'cansaco' in request.POST and request.POST['cansaco'] == 'true' else False
            desconforto = True if 'desconforto' in request.POST and request.POST['desconforto'] == 'true' else False
            dor_garganta = True if 'dor_garganta' in request.POST and request.POST['dor_garganta'] == 'true' else False
            diarreia = True if 'diarreia' in request.POST and request.POST['diarreia'] == 'true' else False
            conjuntivite = True if 'conjuntivite' in request.POST and request.POST['conjuntivite'] == 'true' else False
            dor_cabeca = True if 'dor_cabeca' in request.POST and request.POST['dor_cabeca'] == 'true' else False
            perda_paladar = True if 'perda_paladar' in request.POST and request.POST['perda_paladar'] == 'true' else False
            erupcao_cutanea = True if 'erupcao_cutanea' in request.POST and request.POST['erupcao_cutanea'] == 'true' else False
            falta_ar = True if 'falta_ar' in request.POST and request.POST['falta_ar'] == 'true' else False
            dor_peito = True if 'dor_peito' in request.POST and request.POST['dor_peito'] == 'true' else False
            perda_fala = True if 'perda_fala' in request.POST and request.POST['perda_fala'] == 'true' else False

            exame = Exame(
                febre = febre,
                tosse = tosse,
                cansaco = cansaco,
                desconforto = desconforto,
                dor_garganta = dor_garganta,
                diarreia = diarreia,
                conjuntivite = conjuntivite,
                dor_cabeca = dor_cabeca,
                perda_paladar = perda_paladar,
                erupcao_cutanea = erupcao_cutanea,
                falta_ar = falta_ar,
                dor_peito = dor_peito,
                perda_fala = perda_fala,
                user=request.user
            )

            exame.save()

            calcula_resultado(exame)

            menu_template = loader.get_template('menu.html')
            return HttpResponse(menu_template.render({}, request))

    else:
        login_template = loader.get_template('login.html')
        return HttpResponse(login_template.render({}, request)) 


def menu(request):
    if request.user.is_authenticated:
        template = loader.get_template('menu.html')
        return HttpResponse(template.render({}, request))
    else:
        login_template = loader.get_template('login.html')
        return HttpResponse(login_template.render({}, request)) 


def perfil(request):
    if request.user.is_authenticated:
        
        if request.method == "GET":
            template = loader.get_template('perfil.html')

            context = {
                "email": request.user.email,
                "cpf": request.user.cpf,
                "nome": request.user.nome,
                "telefone": request.user.telefone,
                "endereco": request.user.endereco,
            }

            return HttpResponse(template.render(context, request))

        if request.method == "POST":
            senha = request.POST['senha']
            nome = request.POST['nome']
            telefone = request.POST['telefone']
            endereco = request.POST['endereco']

            usuario = request.user

            usuario.nome = nome
            usuario.telefone = telefone
            usuario.endereco = endereco

            usuario.save()

            if 'senha' in request.POST and senha:
                usuario.set_password(senha)
                usuario.save()

            menu_template = loader.get_template('menu.html')
            return HttpResponse(menu_template.render({}, request))
    else:
        login_template = loader.get_template('login.html')
        return HttpResponse(login_template.render({}, request))


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)

    login_template = loader.get_template('login.html')
    return HttpResponse(login_template.render({}, request)) 
    