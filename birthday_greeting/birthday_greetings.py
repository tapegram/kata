from kata.birthday_greeting.adaptor import EmployeeReaderAdaptor


class BirthdayGreetings(object):

    def __init__(self, employee_repository, email_client):
        employees = EmployeeReaderAdpator(employee_repository).get_employees()
        self.birthday_emails = [
            BirthdayEmail(email_client, employee) for employee in employees
        ]

    def send(self):
        for email in birthday_emails:
            email.send()
