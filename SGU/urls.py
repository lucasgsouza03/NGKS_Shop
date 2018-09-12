from django.conf.urls import url
from SGU.views import *
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^$', sgu, name='sgu'),
    url(r'^chg_pass/', chg_pass, name='chg_pass'),#verificar essa URL
    url(r'^(?P<username>[A-Z,a-z,0-9]+)/detalhes', detalhes, name='detalhes'),
    url(r'^cadastro_usuário/', cadastro_usuario, name='cadastro_usuario'),
    url(r'^login_admin/$', loginAdminPanel, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^erro_acesso/', erro_acesso, name='erro_acesso'),
]