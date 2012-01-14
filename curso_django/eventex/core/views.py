# -*- coding:utf-8 -*-

#ENVIANDO O CONTEXT COM METODOS TRADICIONAIS - RENDERIZANDO O TEMPLATE
'''
from django.http import HttpResponse
from django.template import loader, Context
def homepage(request):
    t = loader.get_template('index.html')
    c = Context()
    content = t.render(c)
    return HttpResponse(content)
'''

#USANDO OS SHORTCUTS (ATALHOS) DO DJANGO PARA RENDERIZAR O TEMPLATE
from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request, template=None):
    from django.conf import settings
    context = RequestContext(request)
    return render_to_response(template, context)
