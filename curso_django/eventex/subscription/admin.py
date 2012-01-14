# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 30/12/11
#Ultima alteracao:

from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

from django.contrib import admin
from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse
from subscription.models import Subscription
import datetime

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today', 'paid') # colunas que aparecerão na listagem
    date_hierarchy = 'created_at' #separa os registros em grupos de datas (ex: agrupa por mes, dia, ano...)
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at') #campos que o search utilizara para buscar os dados
    list_filter = ['created_at']
    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        '''
        Cria nova coluna na listagem "Inscrito Hoje?" e acrescenta um Check (Vezinho) aos que foram inscritos hoje
        '''
        return obj.created_at.date() == datetime.date.today()
    subscribed_today.short_description = 'Inscrito Hoje?'
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        '''
        Marca os registros do Subscription selecionados como sendo Pagos (paid=True)
        '''
        count = queryset.update(paid=True)

        msg = ungettext(
            u'%(count)d inscricao foi marcada como paga.',
            u'%(count)d inscricoes foram marcadas como pagas.',
            count
        ) % {'count': count}
        self.message_user(request, msg)
    mark_as_paid.short_description = _(u"Marcar como pagas")

    def export_subscriptions(self, request):
        subscriptions = self.model.objects.all()
        rows = [','.join([s.name, s.email]) for s in subscriptions]

        response = HttpResponse('\r\n'.join(rows))
        response.mimetype = "text/csv"
        response['Content-Disposition'] = 'attachment; filename=inscricoes.csv'
        return response

    def get_urls(self):
        original_urls = super(SubscriptionAdmin, self).get_urls()
        extra_url = patterns('',
        # envolvemos nossa view em 'admin_view' por que ela faz o
        # controle de permissões e cache para nós
            url(r'exportar-inscricoes/$',
                self.admin_site.admin_view(self.export_subscriptions),
                name='export_subscriptions')
        )
        # A ordem é importante, as urls originais do admin são muito permissivas
        # e acabam sendo encontradas antes das nossas se elas estiverem na frente.
        return extra_url + original_urls

admin.site.register(Subscription, SubscriptionAdmin)
