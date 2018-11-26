from django.shortcuts import render
from src.usuario import Gerencia_permissao
from django.contrib.auth.decorators import login_required, user_passes_test
from SGU.models import Grupos, Usuario, Permissions, Cliente
from catalogo.models import Categoria, Produto
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from SGU.forms import form_cliente, LoginForm, form_usuario
from django.urls import reverse, reverse_lazy
from src.usuario import Gerencia_usuario, Gerencia_permissao
from django.views.generic import CreateView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import contato_forms
from django.views.generic import View, TemplateView, CreateView
from django.contrib import messages
from estoque.models import estoque_produto
from checkout.models import Pedido
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView, ListView, DetailView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def check_estoque(request):
    return 'ESTOQUE' in Gerencia_permissao.Pega_grupo(request)

def check_fluxo(request):
    return 'FLUXO' in Gerencia_permissao.Pega_grupo(request)

def check_pedidos(request):
    return 'PEDIDOS' in Gerencia_permissao.Pega_grupo(request)

def check_empresa(request):
    user = Usuario.objects.get(username=request.username)
    return user.tipo == 'E'

def index(request):
    contexto = {
    'index' : Produto.objects.all().order_by('-criado')[:3],
    }
    return render(request, 'index.html',contexto)

def lista_produtos(request):
    contexto = {
        'lista_produtos': Produto.objects.all()
    }
    return render(request, 'lista_produtos.html', contexto)

def loja_categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    contexto = {
        'categoria_corrente': categoria,
        'lista_produtos': Produto.objects.filter(categoria=categoria),
    }
    return render(request, 'categoria.html', contexto)

def loja_produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    estoque = estoque_produto.objects.filter(produto_id__id=produto.id)
    contexto = {
        'produto': produto,
        'estoque': estoque,
    }
    return render(request, 'produto.html', contexto)

def loginEcommerce(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            account = authenticate(username=username, password=password)
            if account is not None:
                login(request, account)
                return HttpResponseRedirect(reverse('index'))
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

class cadastro_cliente(CreateView):
    form_class = form_cliente
    template_name = 'registro.html'
    success_url = reverse_lazy('index')

registro = cadastro_cliente.as_view() 

def registro(request):    
    if request.method == 'POST':
        form = form_cliente(request.POST)
        if form.is_valid():
            Gerencia_usuario.Cria_cliente(request, form)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('registro'))
    else:
        contexto = {
            "form" : form_cliente(),
            "grupos" : Grupos.objects.all(),
        }            
        return render(request, "registro.html", contexto)

def contato(request):
    success = False
    form = contato_forms(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    else:
        messages.error(request, 'Formulário inválido')
    contexto = {
        'form': form,
        'success': success
    }
    return render(request, 'contato.html', contexto)
    

@login_required(login_url='sgu:login')
@user_passes_test(check_empresa, login_url='sgu:erro_acesso', redirect_field_name=None)
def principal(request):
    return render(request, "principal.html")

@login_required(login_url='sgu:login')
@user_passes_test(check_estoque, login_url='sgu:erro_acesso', redirect_field_name=None)
def estoque(request):
    return render(request, "estoque.html")

@login_required(login_url='sgu:login')
@user_passes_test(check_fluxo, login_url='sgu:erro_acesso', redirect_field_name=None)
def fluxo(request):
    return render(request, "fluxo.html")

@login_required(login_url='sgu:login')
@user_passes_test(check_pedidos, login_url='sgu:erro_acesso', redirect_field_name=None)
def pedidos(request):

    if request.method == 'POST':
        button = request.POST.get("button")
        if button:
            pedido = Pedido.objects.get(pk=button)
            pedido.status = 3
            pedido.save()
    contexto = {
        'pedidos': Pedido.objects.all(),
    }
    return render(request, "pedidos.html", contexto)

def sobre_nos(request):
    return render(request, "sobre_nos.html")

class  Minha_ContaView(LoginRequiredMixin, TemplateView):

    template_name = 'minha_conta.html'

class AtualizarUsuarioView(LoginRequiredMixin, UpdateView):

    model = Usuario
    template_name = 'atualizar_usuario.html'
    fields = ['nome','email']
    success_url = reverse_lazy('minha_conta')
    def get_object(self):
        return self.request.user

class AlterarSenhaView(LoginRequiredMixin, FormView):
    template_name = 'alterar_senha.html'
    success_url = reverse_lazy('minha_conta')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(AlterarSenhaView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AlterarSenhaView, self).form_valid(form)

minha_conta = Minha_ContaView.as_view()
atualizar_usuario = AtualizarUsuarioView.as_view()
alterar_senha = AlterarSenhaView.as_view()