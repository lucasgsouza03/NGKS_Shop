from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from SGU.forms import form_usuario, LoginForm # Formulario de criacao de usuarios
from SGU.models import Grupos, Usuario, Permissions
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from src.usuario import Gerencia_usuario, Gerencia_permissao
from django.urls import reverse

# Create your views here.

#context_processors

def erro_acesso(request):
    return render(request, "erro_acesso.html")

def checa_sgu(request):
    return 'SGU' in Gerencia_permissao.Pega_grupo(request)

@login_required(login_url='sgu:login')
@user_passes_test(checa_sgu, login_url='sgu:erro_acesso', redirect_field_name=None)
def sgu(request):
    contexto = {
        "users" : Usuario.objects.all()
    } 
    delete = request.POST.get("delete")
    if delete:
        Gerencia_usuario.Deleta_usuario(delete)
    return render(request, "sgu.html", contexto)

@login_required(login_url='sgu:login')
@user_passes_test(checa_sgu, login_url='sgu:erro_acesso', redirect_field_name=None)
def cadastro_usuario(request):    
    if request.method == 'POST':
        form = form_usuario(request.POST)
        if form.is_valid():
            Gerencia_usuario.Cria_usuario(request, form)
            return HttpResponseRedirect(reverse('sgu:sgu'))
        else:
            return HttpResponseRedirect(reverse('sgu:cadastro_usuario'))
    else:
        contexto = {
            "form" : form_usuario(),
            "grupos" : Grupos.objects.all(),
        }            
        return render(request, "cadastro_usuario.html", contexto)

@login_required(login_url='sgu:login')
@user_passes_test(checa_sgu, login_url='sgu:erro_acesso', redirect_field_name=None)
def detalhes(request, username):
    if request.method == 'POST':
        button = request.POST.get("button")
        contexto = Gerencia_usuario.Atualiza_usuario(request, username)
        if button == "update_continue":
            return HttpResponseRedirect(reverse('sgu:detalhes', kwargs={'username':username}))
        elif button == "update":
            return HttpResponseRedirect(reverse('sgu:sgu'))
    else:
        perms = []
        grupo = []
        detalhes = Usuario.objects.get(username=username)
        perm = Permissions.objects.filter(usuario_id__id=detalhes.id)
        for i in Grupos.objects.all():
            i = str(i)
            grupo.append(i)
        for i in perm:
            i = str(i)
            perms.append(i)
        contexto = {
            "detalhes" : detalhes,
            "grupos" : grupo,
            "perms" : perms,
        }
    return render(request, "detalhes.html", contexto)

@login_required(login_url='sgu:login')
def chg_pass(request):
    if request.method == 'POST':
        pass_old = request.POST.get("pass_old")
        new_pass = request.POST.get("password")
        if User.check_password(request.user, pass_old):
            user = Usuario.objects.get(username=request.user)
            user.set_password(new_pass)
            user.save()
            return HttpResponseRedirect(reverse('sgu:logout'))
        else:
            print ("Senha incorreta")
    return render(request, "chg_pass.html", contexto)


'''
def loginDashboard(request):
  if request.user.is_authenticated():
    return HttpResponseRedirect('/')
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      account = authenticate(username=username, password=password)
      if account is not None:
        login(request, account)
#here is redirecting to dashboard
          return HttpResponseRedirect('/dashboard/')
      else:
        return render(request, 'profiles/login.html', context)
    else:
      return render(request, 'profiles/login.html', context)
  else:
    form = LoginForm()
    context = {'form':form}
    return render(request, 'profiles/login.html', context)
'''
def loginAdminPanel(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = Usuario.objects.get(username=username)
            if usuario.tipo == 'E':
                account = authenticate(username=username, password=password)
                if account is not None:
                    login(request, account)
                    return HttpResponseRedirect(reverse('principal'))
                else:
                    form = LoginForm()
                    context = {'form':form}
                    return render(request, 'sgu:login.html', context)
            else:
                form = LoginForm()
                context = {'form':form}
                return render(request, 'sgu:login.html', context)
        else:
            form = LoginForm()
            context = {'form':form}
            return render(request, 'sgu:login.html', context)
    else:
        form = LoginForm()
        context = {'form':form}
    return render(request, "login.html", context)