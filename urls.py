# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.auth.views import *
from django.contrib import admin
from TA1.ditex.views import *

admin.autodiscover()

urlpatterns = patterns('',
#	(r'^data/$', data_atual),
#	(r'^data/plus/\d{1,2}/$', horas_depois),
	(r'^admin/', include(admin.site.urls)),
	
	(r'^login', login, { 'template_name': 'login.html' }),
	(r'^sair$', sair),
#	(r'^logout$', logout_then_login, { 'login_url': '/login/' }),
	(r'^inicio$', inicio),
	(r'^servico$', servico),
	
	(r'^lista/(?P<objeto>\w+)$', lista),
	(r'^adiciona/(?P<objeto>\w+)$', adiciona),
	(r'^filtra/(?P<objeto>\w+)', filtra),
	(r'^exibe/(?P<objeto>\w+)/(?P<id_objeto>\d+)/$', exibe),
	(r'^edita/(?P<objeto>\w+)/(?P<id_objeto>\d+)/$', edita),
	(r'^deleta/(?P<objeto>\w+)/(?P<id_objeto>\d+)/$', deleta),

	(r'^servico/oportunidades/abertas$', servico__oportunidades_abertas),
	(r'^servico/exibir/(?P<objeto>\w+)', servico_exibir),
	(r'^servico/cadastrar/(?P<objeto>\w+)', servico_cadastrar),
#	(r'^editora/(?P<id_editora>\d+)/$', editora),
#	(r'^adiciona_livro$', adiciona_livro),
#	(r'^livro/(?P<id_editora>\d+)/$', livro),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	)
