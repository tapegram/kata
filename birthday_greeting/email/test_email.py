from unittest import TestCase
from kata.birthday_greeting.email.email import Email


class DummyEmailClient(object):
    def __init__(self):
        self.call_count = 0

    def send(self, to_field, subject, body):
        self.call_count += 1


class TestEmail(TestCase):

    def test_email(self):
        client = DummyEmailClient()
        self.assertEqual(client.call_count, 0)

        email = Email(client)
        email.send()

        self.assertEqual(client.call_count, 1)


