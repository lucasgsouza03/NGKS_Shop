from django.shortcuts import render
from src.findgroup import get_groups
from django.contrib.auth.decorators import login_required, user_passes_test
from SGU.models import Grupos, Usuario, Permissions

# Create your views here.

def check_estoque(request):
    return 'ESTOQUE' in get_groups(request)

def check_fluxo(request):
    return 'FLUXO' in get_groups(request)

def check_pedidos(request):
    return 'PEDIDOS' in get_groups(request)

def check_empresa(request):
    user = Usuario.objects.get(username=request.username)
    return user.tipo == 'E'

@login_required(login_url='login')
@user_passes_test(check_empresa, login_url='erro_acesso', redirect_field_name=None)
def principal(request):
    return render(request, "principal.html")

@login_required(login_url='login')
@user_passes_test(check_estoque, login_url='erro_acesso', redirect_field_name=None)
def estoque(request):
    return render(request, "estoque.html")

@login_required(login_url='login')
@user_passes_test(check_fluxo, login_url='erro_acesso', redirect_field_name=None)
def fluxo(request):
    return render(request, "fluxo.html")

@login_required(login_url='login')
@user_passes_test(check_pedidos, login_url='erro_acesso', redirect_field_name=None)
def pedidos(request):
    return render(request, "pedidos.html")