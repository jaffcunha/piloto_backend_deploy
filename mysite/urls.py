from django.conf.urls import patterns, include, url
from django.contrib import admin
from sistema.views import *
from sistema.views_membros import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^newapp/', include('newapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^cadastrar_membro/$', 'sistema.views_membros.cadastrar_membro', name='cadastrar_membro'),
	url(r'^editar_membro/(?P<id_pessoa>[0-9]+)/$', 'sistema.views_membros.editar_membro', name='editar_membro'),
	url(r'^excluir_membro/(?P<id_pessoa>[0-9]+)/$', 'sistema.views_membros.excluir_membro', name='excluir_membro'),
	url(r'^visualizar_membros/$', 'sistema.views_membros.visualizar_membros', name='visualizar_membros'),
	url(r'^login/$', 'sistema.views_membros.login', name='login'),
    url(r'^logout/$', 'sistema.views_membros.logout', name='logout'),
	url(r'^home/$', 'sistema.views_membros.home', name='home'),
    url(r'^implementacao_lookup_exact/$', 'sistema.views.implementacao_lookup_exact', name='implementacao_lookup_exact'),
    url(r'^implementacao_lookup_iexact/$', 'sistema.views.implementacao_lookup_iexact', name='implementacao_lookup_iexact'),
    url(r'^implementacao_custom_lookup/$', 'sistema.views.implementacao_custom_lookup', name='implementacao_custom_lookup'),
    url(r'^implementacao_transformacao/$', 'sistema.views.implementacao_transformacao', name='implementacao_transformacao'),
)
