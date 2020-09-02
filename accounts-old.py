import random
import string

from pony.orm import *

from data_source import db


class Role(db.Entity):
    name = Required(str)

    def __str__(self):
        return str(self.name)


class Account(db.Entity):
    role = Required(Role)
    password = Optional(str)

    def create_password(self):
        self.password = self.generate_pass(6)

    def change_password(self, new_password):
        self.password = new_password
        pass

    @staticmethod
    def generate_pass(n: int) -> str:
        return ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(n)))
