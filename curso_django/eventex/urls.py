# -*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from route import route
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^$', 'core.views.homepage', {'template': 'base.html'}),
    #REFATORAÇÃO DA LINHA ACIMA USANDO O METODO ROUTE QUE DEFINE UMA VIEWS ESPECIFICA PARA GET ('new')
    # E OUTRA ESPECÍFICA PARA POST ('create')
    route(r'^$', GET='subscription.views.new', POST='subscription.views.create', name="subscribe"),

    url(r'^inscricao/', include('subscription.urls', namespace='subscription')),

    #url(r'time/$', current_datetime, name="dthr_atual"),
    #url(r'time/plus/(?P<offset>\d{1,2})/(?P<unit>\w+)/$', time_ahead), #passando parametros nomeados para a views
)

urlpatterns += staticfiles_urlpatterns()