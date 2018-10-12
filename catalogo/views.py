from django.shortcuts import render
from src.usuario import Gerencia_permissao
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Produto, Categoria
from src.catalogo import Gerencia_categoria, Gerencia_produto
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def check_catalogo(request):
    return 'CATALOGO' in Gerencia_permissao.Pega_grupo(request)

@login_required(login_url='sgu:login')
@user_passes_test(check_catalogo, login_url='erro_acesso', redirect_field_name=None)
def catalogo(request):
    return render(request, "catalogo.html")

@login_required(login_url='sgu:login')
@user_passes_test(check_catalogo, login_url='erro_acesso', redirect_field_name=None)
def categorias(request):
    contexto = {
        'categorias': Categoria.objects.all()
    }
    delete = request.POST.get("delete")
    if delete:
        Gerencia_categoria.Deleta_categoria(delete)
    return render(request, "categorias.html", contexto)

@login_required(login_url='sgu:login')
@user_passes_test(check_catalogo, login_url='erro_acesso', redirect_field_name=None)
def adiciona_categoria(request):
    if request.method == 'POST':
        Gerencia_categoria.Cria_categoria(request)
        return HttpResponseRedirect(reverse('catalogo:categorias'))
    else:
        return render(request, "adicionar_categoria.html")

@login_required(login_url='sgu:login')
@user_passes_test(check_catalogo, login_url='erro_acesso', redirect_field_name=None)
def categoria_detalhes(request, slug):
    if request.method == 'POST':
        button = request.POST.get("button")
        Gerencia_categoria.Atualiza_categoria(request, slug)
        if button == "update_continue":
            return HttpResponseRedirect(reverse('catalogo:categoria_detalhes', kwargs={'slug':slug}))
        elif button == "update":
            return HttpResponseRedirect(reverse('catalogo:categorias'))
    else:
        contexto = {
            'categoria': Categoria.objects.get(slug=slug)
        }
        return render(request, "categoria_detalhes.html", contexto)

@login_required(login_url='sgu:login')
@user_passes_test(check_catalogo, login_url='erro_acesso', redirect_field_name=None)
def produtos(request):
    contexto = {
        'produtos': Produto.objects.all()
    }
    delete = request.POST.get("delete")
    if delete:
        Gerencia_produto.Deleta_produto(delete)
    return render(request, "produtos.html", contexto)

def adiciona_produto(request):
    if request.method == 'POST':
        Gerencia_produto.Cria_produto(request)
        return HttpResponseRedirect(reverse('catalogo:produtos'))
    else:
        contexto = {
            'categorias': Categoria.objects.all()
        }
        return render(request, "adicionar_produto.html", contexto)

def produto_detalhes(request, slug):
    if request.method == 'POST':
        button = request.POST.get("button")
        Gerencia_produto.Atualiza_produto(request, slug)
        if button == "update_continue":
            return HttpResponseRedirect(reverse('catalogo:produto_detalhes', kwargs={'slug':slug}))
        elif button == "update":
            return HttpResponseRedirect(reverse('catalogo:produtos'))
    else:
        produto = Produto.objects.get(slug=slug)
        contexto = {
            'categorias': Categoria.objects.all(),
            'produto': produto,
            'price': int(produto.price)
        }
        return render(request, "produto_detalhes.html", contexto)