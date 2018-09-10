from django.conf.urls import url
from SGU.views import *
from django.contrib.auth.views import login,logout
from django.contrib.auth import views as auth_views 

urlpatterns = [
    url(r'^password_reset/$', auth_views.password_reset, {'subject_template_name': 'password_reset_subject.txt'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^$', sgu, name='sgu'),
    url(r'^chg_pass/', chg_pass, name='chg_pass'),
    url(r'^(?P<username>[A-Z,a-z,0-9]+)/detalhes', detalhes, name='detalhes'),
    url(r'^cadastro_user/', cadastro_user, name='cadastro_user'),
    url(r'^login_admin/$', loginAdminPanel, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^erro_acesso/', erro_acesso, name='erro_acesso'),
]