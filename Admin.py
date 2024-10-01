from User import User

class Admin(User):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 999999999