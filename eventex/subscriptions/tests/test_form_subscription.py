from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        form = SubscriptionForm()
        """O formulario deve ter 4 campos"""
        expected = ['name','cpf','email','phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        ''' CPF deve aceitar apenas digitos'''
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertEqual(['cpf'],list(form.errors))
        #self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas números')
        self.assertFormErrorCode(form, 'cpf', 'digits')


    def test_cpf_has_11_digits(self):
        ''' CPF deve conter 11 digitos'''
        form = self.make_validated_form(cpf='1234')
        #self.assertFormErrorMessage(form, 'cpf', 'CPF deve ter 11 (onze) números')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):

        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)




    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = data = dict(name='Orlando Saboia', cpf='12455678901',
                    email='fobs@bol.com.br', phone='86-12345-6789')

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

