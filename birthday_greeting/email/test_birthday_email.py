from unittest import TestCase
from kata.birthday_greeting.birthday_email import BirthdayEmail
from kata.birthday_greeting.employee import Employee


class DummyEmailClient(object):
    def __init__(self):
        self.call_count = 0
        self.to_field = None
        self.subject = None
        self.body = None

    def send(self, to_field, subject, body):
        self.call_count += 1
        self.to_field = to_field
        self.subject = subject
        self.body = body


class TestBirthdayEmail(TestCase):

    def test_birthday_email(self):
        client = DummyEmailClient()
        self.assertEqual(client.call_count, 0)
        self.assertIsNone(client.to_field)
        self.assertIsNone(client.subject)
        self.assertIsNone(client.body)

        employee = Employee(
            "Pegram", "Tavish", "10/11/1991", "a@b.com")
        email = BirthdayEmail(client, employee)
        email.send()

        self.assertEqual(client.call_count, 1)
        self.assertEqual(client.to_field, "a@b.com")
        self.assertEqual(client.subject, "Happy birthday!")
        self.assertEqual(client.body, "Happy birthday, dear Tavish")

