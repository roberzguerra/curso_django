# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 28/12/11
#Ultima alteracao:

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('subscription.views',
    url(r'^$', 'subscribe', name="subscribe"),
    url(r'^(\d+)/sucesso/$', 'success', name="success"),
)

