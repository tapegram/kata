from kata.birthday_greeting.employee.employee import Employee


class EmployeeReaderAdaptor(object):
    def __init__(self, reader):
        self.reader = reader

    def get_employees(self):
        employee_list = self.reader.read()

        return [
            Employee(
                last_name=employee[0],
                first_name=employee[1],
                date_of_birth=employee[2],
                email=employee[3]) for employee in employee_list
        ]
