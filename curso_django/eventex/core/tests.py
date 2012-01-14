# -*- coding:utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

#exemplo de teste
'''
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
'''

class HomepageUrlTest(TestCase):
    def test_success_when_get_homepage(self):
        #emula uma requisicao http passando o caminho ('/') da requisicao, e armazena no response
        response = self.client.get('/')

        #verifica o status_code do request, no caso esta exigindo que 2000 seja igual ao status_code
        #quando essa exigencia não é respeitada o teste falha
        self.assertEquals(200, response.status_code)

        #garante que a resposta seja renderizada utilizando o template 'index.html'
        self.assertTemplateUsed(response, 'index.html')
