from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeGet(TestCase):

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
        tags = (('<form',1),
                ('<input',6),
                ('type="text"', 3),
                ('type="email"',1),
                ('type="submit"',1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

        # Test antes do for acima
        #self.assertContains(self.resp, '<form')
        #self.assertContains(self.resp, '<input',6)
        #self.assertContains(self.resp,'type="text"', 3)
        #self.assertContains(self.resp, 'type="email"')
        #self.assertContains(self.resp,'type="submit"')

    def test_csrf(self):
        """ HTML deve ter csrf"""
        self.assertContains(self.resp,'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context deve ter subscription form """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)



class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Orlando Saboia', cpf='12345678901',
                    email='fobs@bol.com.br', phone='86-12345-6789')

        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Post valido redirecionar para /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))


class SubscribePostInvalid(TestCase):
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

