from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import cadastrar_fornecedor
from src.estoque import Gerencia_fornecedor
from src.usuario import Gerencia_permissao
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import fornecedor

# Create your views here.

def check_estoque(request):
    return 'ESTOQUE' in Gerencia_permissao.Pega_grupo(request)

@login_required(login_url='sgu:login')
@user_passes_test(check_estoque, login_url='sgu:erro_acesso', redirect_field_name=None)
def estoque(request):
    return render(request, "estoque.html")

@login_required(login_url='sgu:login')
@user_passes_test(check_estoque, login_url='sgu:erro_acesso', redirect_field_name=None)
def fornecedores(request):
    contexto = {
        'fornecedores': fornecedor.objects.all(),
    }
    delete = request.POST.get("delete")
    if delete:
        Gerencia_fornecedor.Deleta_fornecedor(delete)
    return render(request, "fornecedor.html", contexto)

@login_required(login_url='sgu:login')
@user_passes_test(check_estoque, login_url='sgu:erro_acesso', redirect_field_name=None)
def cadastro_fornecedor(request):
    if request.method == 'POST':
        form = cadastrar_fornecedor(request.POST)    
        if form.is_valid():
            print("forms válido")
            form.save()
            return HttpResponseRedirect(reverse('estoque:fornecedores'))
        else:
            print("forms inválido")
            return HttpResponseRedirect(reverse('estoque:cadastro_fornecedor'))
    contexto= {
        'form':cadastrar_fornecedor()
    }
    return render(request, "cadastro_fornecedor.html", contexto)


@login_required(login_url='sgu:login')
@user_passes_test(check_estoque, login_url='sgu:erro_acesso', redirect_field_name=None)
def fornecedor_detalhes(request, slug):
    if request.method == 'POST':
        button = request.POST.get("button")
        Gerencia_fornecedor.Atualiza_fornecedor(request, slug)
        if button == "update_continue":
            return HttpResponseRedirect(reverse('estoque:fornecedor_detalhes', kwargs={'slug':slug}))
        elif button == "update":
            return HttpResponseRedirect(reverse('estoque:fornecedores'))
    else:
        contexto = {
            'fornecedor': fornecedor.objects.get(slug=slug)
        }
    return render(request, 'fornecedor_detalhes.html', contexto)


