from unittest import TestCase
from kata.birthday_greeting.birthday_greetings import BirthdayGreetings
from kata.birthday_greeting.reader.employee_reader_adapter import EmployeeReaderAdaptor
from kata.birthday_greeting.employee.employee import Employee


class DummyReader(object):
    def read(self):
        return [
            ["Smith", "John", "10/11/1991", "john@gmail.com"],
            ["Donaldson", "Fred", "09/17/1989", "fred@gmail.com"],
        ]


class DummyEmailClient(object):
    def __init__(self):
        self.call_count = 0
        self.call_args = []

    def send(self, to_field, subject, body):
        self.call_count += 1
        self.call_args.append(
        [to_field, subject, body])

class TestBirthdayGreetings(TestCase):

    def test_birthday_greetings(self):
        reader = DummyReader()
        client = DummyEmailClient()
        birthday_greetings = BirthdayGreetings(
            reader, client)

        self.assertEqual(len(birthday_greetings.birthday_emails), 2)

        birthday_greetings.send()
        self.assertEqual(client.call_count, 2)
        self.assertEqual(len(client.call_args), 2)
        self.assertListEqual(
            client.call_args[0],
            ["john@gmail.com", "Happy birthday!", "Happy birthday, dear John"])
        self.assertListEqual(
            client.call_args[1],
            ["fred@gmail.com", "Happy birthday!", "Happy birthday, dear Fred"])


