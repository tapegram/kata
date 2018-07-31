class Email(object):

    def __init__(self,
                 client):
        self.client = client

    def send(self):
         self.client.send(
             self.to_field, self.subject, self.body)

    @property
    def to_field(self):
        pass

    @property
    def subject(self):
        pass

    @property
    def body(self):
        pass
