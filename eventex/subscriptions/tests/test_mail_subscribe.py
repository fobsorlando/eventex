from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Orlando Saboia', cpf='12345678901',
                    email='fobs@bol.com.br', phone='86-12345-6789')

        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmacao de Inscricao'

        self.assertEqual(expect,self.email.subject)


    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','fobs@bol.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Orlando Saboia',
            '12345678901',
            'fobs@bol.com.br',
            '86-12345-6789'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

