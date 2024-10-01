from User import User

class Customer(User):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = None