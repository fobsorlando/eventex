from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Orlando Saboia',
            cpf = '1234567890',
            email = 'orlandosaboia@gmail.com',
            phone = '86123456789'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """ Subscription deve ter um auto created_at atributo"""
        self.assertIsInstance(self.obj.created_at, datetime)

