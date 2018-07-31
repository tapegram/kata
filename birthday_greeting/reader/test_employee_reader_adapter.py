from unittest import TestCase
from kata.birthday_greeting.reader.employee_reader_adapter import EmployeeReaderAdaptor
from kata.birthday_greeting.employee.employee import Employee


class DummyReader(object):
    def read(self):
        return [
            ["Smith", "John", "10/11/1991", "john@gmail.com"],
            ["Donaldson", "Fred", "09/17/1989", "fred@gmail.com"],
        ]


class TestEmployeeReadAdaptor(TestCase):

    def test_get_employees(self):
        reader = EmployeeReaderAdaptor(DummyReader())
        employees = reader.get_employees()

        self.assertEqual(len(employees), 2)
        employee_1 = employees[0]
        employee_2 = employees[1]

        self.assertEqual(employee_1.last_name, "Smith")
        self.assertEqual(employee_1.first_name, "John")
        self.assertEqual(employee_1.date_of_birth, "10/11/1991")
        self.assertEqual(employee_1.email, "john@gmail.com")

        self.assertEqual(employee_2.last_name, "Donaldson")
        self.assertEqual(employee_2.first_name, "Fred")
        self.assertEqual(employee_2.date_of_birth, "09/17/1989")
        self.assertEqual(employee_2.email, "fred@gmail.com")

