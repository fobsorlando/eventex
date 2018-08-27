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

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Orlando Saboia',
            slug='orlando-saboia',
            photo='https://www.aereo.jor.br/wp-content/uploads//2018/08/Spanish-Air-Force-Eurofighter-Typhoon.jpg'
        )

        s.contact_set.create(kind=Contact.EMAIL, value = 'orlandosaboia@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value = '86-123456789')


    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['orlandosaboia@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['86-123456789']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
