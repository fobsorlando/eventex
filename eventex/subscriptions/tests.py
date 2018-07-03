from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTests(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        '''get '''
        self.assertEqual(200,self.resp.status_code)

    def teste_template(self):
        """ use subscriptios/"""
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    def test_html(self):
        """ htm dev conter imput tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input',6)
        self.assertContains(self.resp,'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp,'type="submit"')

    def test_csrf(self):
        """ HTML deve ter csrf"""
        self.assertContains(self.resp,'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context deve ter subscription form """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """O formulario deve ter 4 campos"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'],list(form.fields))

class SubscribePostTest(TestCase):

    def setUp(self):
        data = dict(name='Orlando Saboia', cpf='12345678901',
                    email='fobs@bol.com.br', phone='86-12345-6789')

        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Post valido redirecionar para /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmacao de Inscricao'

        self.assertEqual(expect,email.subject)


    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br','fobs@bol.com.br']

        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]


class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/',{})
    def test_post(self):
        """Post invalido nao deve redirecionar"""

        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form  = self.resp.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Orlando Saboia', cpf ='12345678901',
                    email='fobs@bol.com.br', phone = '86-12345-6789')

        response = self.client.post('/inscricao/', data, follow=True)

        self.assertContains(response,'Inscrição Realizada com Sucesso!')


