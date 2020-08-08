import random


class Account:
    def __init__(self, role: Role):
        self.password = self.generate_pass(6)
        self.role = role
        self.id = id(self)

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    def get_id(self):
        return self.id

    def set_password(self, new_password):
        self.password = new_password

    def change_password(self, new_password):
        self.set_password(new_password)
        pass

    @staticmethod
    def generate_pass(n: int) -> str:
        return ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(n)))


class Role:
    def __init__(self, name):
        self.name = name
        self.id = id(self)

    def get_name(self):
        return self.name
