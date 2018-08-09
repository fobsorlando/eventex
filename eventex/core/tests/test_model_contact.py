from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import  Speaker, Contact


class ContactModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name = 'Orlando Saboia',
            slug = 'orlando-saboia',
            photo = 'https://www.aereo.jor.br/wp-content/uploads//2018/08/Spanish-Air-Force-Eurofighter-Typhoon.jpg'
        )

    def teset_email(self):
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind = Contact.EMAIL,
            value = 'orlandosaboia@gmail.com'
        )
        self.assertTrue(Contact.objects.exists())

    def teset_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE ,
            value='86-123456789'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        '''Campo KIND do contato deve ser apenas E ou P'''
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,
            kind=Contact.EMAIL,
            value='orlandosaboia@gmail.com'
        )
        self.assertEqual('orlandosaboia@gmail.com', str(contact))

