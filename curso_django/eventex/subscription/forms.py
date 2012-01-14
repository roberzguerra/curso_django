# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 29/12/11
#Ultima alteracao:

from django import forms
from django.utils.translation import ugettext as _
from subscription import validators
from subscription.models import Subscription

#class SubscriptionForm(forms.ModelForm):
#    teste = forms.CheckboxSelectMultiple()
#    class Meta:
#        model = Subscription
#        exclude = ('created_at',)

#class SubscriptionForm(forms.Form):
#    name = forms.CharField(label=_("Nome:"), max_length=100)
#    cpf = forms.CharField(label=_("CPF:"), validators=[validators.CpfValidator])
#    email = forms.CharField(label=_("E-mail:"))
#    phone = forms.CharField(label=_("Telefone:"), required=False, max_length=20)
#    LINHAS ACIMAS ALTERADAS PARA:

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('crated_at', 'paid')

    def clean(self):
        # CHAMANDO ESTE SUPER ELE EXECUTA O CLEAN() E DEPOIS CHAMA O SAVE() ORIGINAL DO MODEL
        # PARA ENTÃO PERSISTIR (GRAVAR) NO BANCO DE DADOS
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise forms.ValidationError(
                _(u"Informe E-mail ou Telefone.")
            )
        return self.cleaned_data


#
#    Estes metodos foram substituídos pelos logo abaixo...
#    def clean_cpf(self):
#        try:
#            s = Subscription.objects.get(cpf=self.cleaned_data['cpf'])
#        except Subscription.DoesNotExist:
#            return self.cleaned_data['cpf']
#        raise forms.ValidationError(_(u"Esta CPF já está cadastrado."))
#
#    def clean_email(self):
#        try:
#            s = Subscription.objects.get(email=self.cleaned_data['email'])
#        except Subscription.DoesNotExist:
#            return self.cleaned_data['email']
#        raise forms.ValidationError(_(u"Este e-mail já está cadastrado."))


#   METODO QUE SUBSTITUI OS ACIMA:


    def _unique_check(self, fieldname, error_message):
        '''
        ATENÇÃO *********************************************
            não precisa fazer isso se vc tiver um model com a propriedade unique=true setada,
            pois o django ja faz automático, mas se vc tiver um form personalizado, que nao
            herde de um model que tenha o unique true para o field especifico então deve se
            implementar este metodo.

        ATENÇÃO_2 ******************************************
            este metod está definido como privano nos padrões pythonicos,
            o _ (underline) na frente indica que é privado portanto não se deve chamado
            fora desta classe.
            Isso porque ele pode ser alterado a qualquer momento, então deste modo só
            será preciso alterar suas chamadas dentro desta classe.
        '''

        param = { fieldname : self.cleaned_data[fieldname] }
        try:
            s = Subscription.objects.get(**param)
            # os ** (dois asteriscos) fazem o unpecking do dicionario acima: param = { fieldname : self.cleaned_data[fieldname] }
            # vai transformar o dicionario em: cpf=self.cleaned_data['cpf']
            # ou seja, a chave recebe o valor

        except Subscription.DoesNotExist:
            return self.cleaned_data[ fieldname ]
        raise forms.ValidationError( error_message )

    def clean_cpf(self):
        return self._unique_check('cpf', _(u"CPF já cadastrado."))

    def clean_email(self):
        return self._unique_check('email', _(u"E-mail já cadastrado."))
