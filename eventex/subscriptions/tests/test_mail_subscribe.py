from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Diogenes', cpf='12345678901',
                    email='dio.a100@gmail.com', phone='11-976407547')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'dio.a100@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_body(self):

        contents = [
            'Diogenes',
            '12345678901',
            'dio.a100@gmail.com',
            '11-976407547',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)