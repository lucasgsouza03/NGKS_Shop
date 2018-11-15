from django.conf.urls import url
from catalogo.views import *

urlpatterns = [
    url(r'^$', catalogo, name='catalogo'),
    url(r'categorias/$', categorias, name='categorias'),
    url(r'^(?P<slug>[\w_-]+)/categoria_detalhes', categoria_detalhes, name='categoria_detalhes'),
    url(r'adiciona_categoria/$', adiciona_categoria, name='adiciona_categoria'),
    url(r'^produtos/$', produtos, name='produtos'),
    url(r'^(?P<slug>[\w_-]+)/produto_detalhes', produto_detalhes, name='produto_detalhes'),
    url(r'adiciona_produto/$', adiciona_produto, name='adiciona_produto'),
]