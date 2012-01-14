# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 11/01/12
#Ultima alteracao:


from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

def CpfValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u"O CPF deve conter apenas números."))
    if len(value) != 11:
        raise ValidationError(_(u"O CPF deve ter 11 dígitos."))
