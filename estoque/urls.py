from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', estoque, name='estoque'),
    url(r'^fornecedores/$', fornecedores, name='fornecedores'),
    url(r'^cadastro_forncedor/$', cadastro_fornecedor, name='cadastro_fornecedor'),
    url(r'^(?P<slug>[\w_-]+)/fornecedor_detalhes', fornecedor_detalhes, name='fornecedor_detalhes'),
]