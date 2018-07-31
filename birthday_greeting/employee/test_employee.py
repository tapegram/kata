from unittest import TestCase
from kata.birthday_greeting.employee.employee import Employee


class TestEmployee(TestCase):

    def test_employee(self):
        employee = Employee(
            "last", "first", "dob", "a@b.com")

        self.assertEqual(employee.last_name, "last")
        self.assertEqual(employee.first_name, "first")
        self.assertEqual(employee.date_of_birth, "dob")
        self.assertEqual(employee.email, "a@b.com")
