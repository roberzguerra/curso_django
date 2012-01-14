# -*- encoding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from forms import SubscriptionForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from subscription.models import Subscription
from django.utils.translation import ugettext as _


#METODO CHAMADO PELA URL
def subscribe(request):
    if request.method=='POST':
        return create(request)
    else:
        return new(request)

#METODO QUE MONTA A TELA COM OS CAMPOS LIMPOS
def new(request):
#    form = SubscriptionForm()

#    O form tem 2 estados:
#     - Bounded Form:
#        quando o form recebe dados, como o request.POST, ex:
#            form = SubscriptionForm(request.POST)
#        OBS: o exemplo form = SubscriptionForm(initial={...}) NÃO gera Bounded Form, pois os dados não vão para o
#        clean_data do form
#
#     - Ungounded Form:
#        quando o form é inicializado vazio, ex:
#            form = SubscriptionForm()

    #inicializando o form
    #neste caso seria legal adicionar no template .html um javascript que limpasse os campos ao clicar neles.
    form = SubscriptionForm(initial={
        'name': _(u"Entre o seu nome"),
        'cpf': _(u"Digite o seu CPF sem pontos ou traços"),
        'email': _(u"Informe o seu e-mail"),
        'phone': _(u"Informe seu telefone para contato"),
    })

    context = RequestContext(request, {'form':form})
    return render_to_response('subscription/new.html', context)

#METODO QUE CRIA E SALVA O SUBSCRIBE
def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form':form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()

    #enviando email depois de salvar
    from django.core.mail import send_mail
    send_mail(
        subject=u"Inscrição no EventeX",
        message=u"Obrigado por se inscrever no EventeX!",
        from_email='rober_zg@yahoo.com.br',
        recipient_list=[ subscription.email ],
    )

    return HttpResponseRedirect(
        reverse('subscription:success', args=[subscription.pk])
    )

#CÓDIGO ANTIGO A REFATORAÇÃO ONDE FOI SEPARADO NOS METODOS new() e create()
'''
def subscribe(request):
    if request.method=='POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            return HttpResponseRedirect(
                reverse('subscription:success', args=[subscription.pk])
            )
    else:
        form = SubscriptionForm()

    context = RequestContext(request, {'form':form})
    return render_to_response('subscription/new.html', context)
'''


def success(request, pk):

    subscription = get_object_or_404(Subscription, pk=pk) # Se a pk existir retorna o objeto Subscription, se não
    # da um erro 404 dizendo que não existe a pagina solicitada
    # esta passando um model (Subscription), mas tbm aceita querysets

    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)