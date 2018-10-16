"""NGKS_Shop path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.paths import include, path
    2. Add a path to pathpatterns:  path('blog/', include('blog.paths'))
"""
from django.conf.urls import url, include
from core.views import *
from django.contrib.auth.views import logout

urlpatterns = [
    #ecommerce
    url(r'^$', index, name='index'),
    url(r'^lista_produtos/', lista_produtos, name='lista_produtos'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$', loja_categoria, name='loja_categoria'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', loja_produto, name='loja_produto'),
    url(r'^registro/', registro, name='cadastro_cliente'),
    url(r'^login/$', loginEcommerce, name='loginEcommerce'),
    url(r'^logout/$', logout, {'next_page': 'index'} ,name='logout'),
    url(r'^contato/$', contato,name='contato'),
    url(r'^checkout/', include(('checkout.urls', 'checkout'), namespace='checkout')),
    #administrativo
    url(r'^principal/$', principal, name='principal'),
    url(r'^sgu/', include(('SGU.urls', 'sgu'), namespace='sgu')),
    url(r'^estoque/$', estoque, name='estoque'),
    url(r'^fluxo/$', fluxo, name='fluxo'),
    url(r'^pedidos/$', pedidos, name='pedidos'),
    url(r'^catalogo/', include(('catalogo.urls', 'catalogo'), namespace='catalogo')),
]