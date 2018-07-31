from kata.birthday_greeting.email import Email


class BirthdayEmail(Email):

    def __init__(
            self,
            client,
            employee):
        self.employee = employee
        super(BirthdayEmail, self).__init__(
            self, client)

    @property
    def to_field(self):
        return employee.email

    @property
    def subject(self):
        return "Happy birthday!"

    @property
    def body(self):
        return "Happy birthday, dear {}".format(self.employee.first_name)
