from django.conf.urls import patterns, include, url
from perfis import views

urlpatterns = patterns('',
    # url(r'^$', 'perfis.views.index', name='index'),
    # url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir', name='exibir'),
    # url(r'^perfis/(?P<perfil_id>\d+)/convidar$', 'perfis.views.convidar', name='convidar')
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar')    
)
