from kata.birthday_greeting.email.email import Email


class BirthdayEmail(Email):

    def __init__(
            self,
            client,
            employee):
        self.employee = employee
        super(BirthdayEmail, self).__init__(client)

    @property
    def to_field(self):
        return self.employee.email

    @property
    def subject(self):
        return "Happy birthday!"

    @property
    def body(self):
        return "Happy birthday, dear {}".format(self.employee.first_name)
