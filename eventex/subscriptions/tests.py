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