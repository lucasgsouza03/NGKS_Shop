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
from django.contrib.auth import views as auth_views 

urlpatterns = [
    url(r'^sgu/', include(('SGU.urls', 'sgu'), namespace='sgu')),
    url(r'^principal/estoque/$', estoque, name='estoque'),
    url(r'^principal/fluxo/$', fluxo, name='fluxo'),
    url(r'^principal/pedidos/$', pedidos, name='pedidos'),
    url(r'^principal/$', principal, name='principal'),
    url(r'^password_reset/$', auth_views.password_reset, {'subject_template_name': 'password_reset_subject.txt'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]