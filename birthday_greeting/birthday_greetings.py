from kata.birthday_greeting.reader.employee_reader_adapter import EmployeeReaderAdaptor
from kata.birthday_greeting.email.birthday_email import BirthdayEmail


class BirthdayGreetings(object):

    def __init__(self, employee_repository, email_client):
        employees = EmployeeReaderAdaptor(employee_repository).get_employees()
        self.birthday_emails = [
            BirthdayEmail(email_client, employee) for employee in employees
        ]

    def send(self):
        for email in self.birthday_emails:
            email.send()
