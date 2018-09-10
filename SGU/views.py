from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from SGU.forms import cadasto_user, LoginForm # Formulario de criacao de usuarios
from SGU.models import Grupos, Usuario, Permissions
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from src.findgroup import get_groups
from django.urls import reverse

# Create your views here.

#context_processors

def erro_acesso(request):
    return render(request, "erro_acesso.html")

def check_sgu(request):
    return 'SGU' in get_groups(request)

@login_required(login_url='login')
@user_passes_test(check_sgu, login_url='erro_acesso', redirect_field_name=None)
def sgu(request):
    contexto = {
        "users" : Usuario.objects.all()
    } 
    delete = request.POST.get("delete")
    if delete:
        Permissions.objects.filter(usuario_id=delete).delete()
        Usuario.objects.filter(id=delete).delete()
    return render(request, "sgu.html", contexto)

@login_required(login_url='login')
@user_passes_test(check_sgu, login_url='erro_acesso', redirect_field_name=None)
def cadastro_user(request):
    
    if request.method == 'POST':
        form = cadasto_user(request.POST)
        if form.is_valid():
            nome = request.POST.getlist("grupo")
            form.save()
            username = request.POST.get("username")
            pessoa = Usuario.objects.get(username=username)
            pessoa.tipo = 'E'
            pessoa.save()
            for i in nome:
                done = Permissions.objects.create(groups=i, usuario_id=pessoa.id)
                done.save()
            return HttpResponseRedirect(reverse('sgu:sgu'))
        else:
            return HttpResponseRedirect(reverse('sgu:cadastro_user'))
    else:
        contexto = {
            "form" : cadasto_user(),
            "grupos" : Grupos.objects.all(),
        }            
        return render(request, "cadastro_user.html", contexto)

@login_required(login_url='login')
@user_passes_test(check_sgu, login_url='erro_acesso', redirect_field_name=None)
def detalhes(request, username):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        perm_update = request.POST.getlist("grupo")
        button = request.POST.get("button")
        is_active = request.POST.get("is_active")
        pessoa = Usuario.objects.get(username=username)
        perms = []
        grupo = []
        for i in Permissions.objects.filter(usuario_id__id=pessoa.id):
            i = str(i)
            perms.append(i)
        for i in perms:
            if i not in perm_update:
                Permissions.objects.filter(usuario_id__id=pessoa.id, groups=i).delete()
        for i in perm_update:
            if i not in perms:
                Permissions.objects.create(groups=i, usuario_id=pessoa.id)
        for i in Grupos.objects.all():
            i = str(i)
            grupo.append(i)
        for i in Permissions.objects.filter(usuario_id__id=pessoa.id):
            i = str(i)
            perms.append(i)
        if is_active == "on":
            pessoa.is_active = 1
        elif is_active is None:
            pessoa.is_active = 0
        pessoa.nome = nome
        pessoa.email = email
        pessoa.save()
        contexto = {
            "detalhes" : pessoa,
            "grupos" : grupo,
            "perms" : perms,
        }
        if button == "update_continue":
            return HttpResponseRedirect(reverse('sgu:detalhes'))
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

@login_required(login_url='login')
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
            user = Usuario.objects.get(username=username)
            if user.tipo == 'E':
                account = authenticate(username=username, password=password)
                if account is not None:
                    login(request, account)
                    return HttpResponseRedirect(reverse('principal'))
                else:
                    form = LoginForm()
                    context = {'form':form}
                    return render(request, 'login.html', context)
            else:
                form = LoginForm()
                context = {'form':form}
                return render(request, 'login.html', context)
        else:
            form = LoginForm()
            context = {'form':form}
            return render(request, 'login.html', context)
    else:
        form = LoginForm()
        context = {'form':form}
    return render(request, 'login.html', context)