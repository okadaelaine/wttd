from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Elaine Okada', cpf='12345678901',
                    email='3l41n3@gmail.com', phone='11-12345-1234')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', '3l41n3@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Elaine Okada',
                    '12345678901',
                    '3l41n3@gmail.com',
                    '11-12345-1234']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
