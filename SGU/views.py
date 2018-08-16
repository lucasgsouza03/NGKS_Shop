from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from SGU.forms import cadasto_user # Formulario de criacao de usuarios
from SGU.models import grupos, usuario, Permissions
from django.contrib.auth import authenticate

# Create your views here.

def header(request):
    perm = Permissions.objects.filter(usuario_id__username=request.user)
    grupo = grupos.objects.all()
    contexto = {'perm':perm, 'grupo': grupo}
    return contexto

def erro_acesso(request):
    return render(request, "erro_acesso.html")

def get_groups(request):
    perm = Permissions.objects.filter(usuario_id__username=request.username)
    grupos = []
    for i in perm:
        i = str(i)
        grupos.append(i)
    return grupos

def check_sgu(request):
    return 'SGU' in get_groups(request)

def check_estoque(request):
    return 'ESTOQUE' in get_groups(request)

def check_fluxo(request):
    return 'FLUXO' in get_groups(request)

def check_pedidos(request):
    return 'PEDIDOS' in get_groups(request)

@login_required(login_url='/login')
@user_passes_test(check_sgu, login_url='/erro_acesso', redirect_field_name=None)
def sgu(request):
    contexto = header(request)
    contexto["users"] = usuario.objects.all()
    delete = request.POST.get("delete")
    if delete:
        Permissions.objects.filter(usuario_id=delete).delete()
        usuario.objects.filter(id=delete).delete()
    return render(request, "sgu.html", contexto)

@login_required(login_url='/login')
@user_passes_test(check_sgu, login_url='/erro_acesso', redirect_field_name=None)
def cadastro_user(request):
    
    if request.method == 'POST':
        form = cadasto_user(request.POST)
        if form.is_valid():
            nome = request.POST.getlist("grupo") 
            form.save()
            username = request.POST.get("username")
            pessoa = usuario.objects.get(username=username)
            for i in nome:
                done = Permissions.objects.create(groups=i, usuario_id=pessoa.id)
                done.save()
            return HttpResponseRedirect("/principal/sgu")
    else:
        contexto = header(request)
        contexto["form"] =  cadasto_user()
        contexto["grupos"] = grupos.objects.all()
            
        return render(request, "cadastro_user.html", contexto)

@login_required(login_url='/login')
@user_passes_test(check_sgu, login_url='/erro_acesso', redirect_field_name=None)
def detalhes(request, username):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        perm_update = request.POST.getlist("grupo")
        button = request.POST.get("button")
        is_active = request.POST.get("is_active")
        pessoa = usuario.objects.get(username=username)
        contexto = header(request)
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
        for i in grupos.objects.all():
            i = str(i)
            grupo.append(i)
        for i in Permissions.objects.filter(usuario_id__id=pessoa.id):
            i = str(i)
            perms.append(i)
        print(pessoa.id)
        if is_active == "on":
            pessoa.is_active = 1
        elif is_active is None:
            pessoa.is_active = 0
        pessoa.nome = nome
        pessoa.email = email
        pessoa.save()
        contexto["detalhes"] = pessoa
        contexto["grupos"] = grupo
        contexto["perms"] = perms
        if button == "update_continue":
            return HttpResponseRedirect("detalhes")
        elif button == "update":
            return HttpResponseRedirect("/principal/sgu/")
    else:
        contexto = header(request)
        perms = []
        grupo = []
        detalhes = usuario.objects.get(username=username)
        perm = Permissions.objects.filter(usuario_id__id=detalhes.id)
        for i in grupos.objects.all():
            i = str(i)
            grupo.append(i)
        for i in perm:
            i = str(i)
            perms.append(i)
        contexto["detalhes"] = detalhes
        contexto["grupos"] = grupo
        contexto["perms"] = perms
    return render(request, "detalhes.html", contexto)

@login_required(login_url='/login')
def principal(request):
    contexto = header(request)
    return render(request, "principal.html", contexto)

@login_required(login_url='/login')
def chg_pass(request):
    if request.method == 'POST':
        pass_old = request.POST.get("pass_old")
        new_pass = request.POST.get("password")
        contexto = header(request)
        if User.check_password(request.user, pass_old):
            user = usuario.objects.get(username=request.user)
            user.set_password(new_pass)
            user.save()
            return HttpResponseRedirect("/logout")
        else:
            print ("Senha incorreta")
    contexto = header(request)
    return render(request, "chg_pass.html", contexto)

@login_required(login_url='/login')
@user_passes_test(check_estoque, login_url='/erro_acesso', redirect_field_name=None)
def estoque(request):
    contexto = header(request)
    return render(request, "estoque.html", contexto)

@login_required(login_url='/login')
@user_passes_test(check_fluxo, login_url='/erro_acesso', redirect_field_name=None)
def fluxo(request):
    contexto = header(request)
    return render(request, "fluxo.html", contexto)

@login_required(login_url='/login')
@user_passes_test(check_pedidos, login_url='/erro_acesso', redirect_field_name=None)
def pedidos(request):
    contexto = header(request)
    return render(request, "pedidos.html", contexto)