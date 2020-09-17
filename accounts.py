import random
import string
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

import db_bind


class Role(db_bind.Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    account_id = Column(Integer, ForeignKey('accounts.id'))

    account = relationship("Account", back_populates="role")

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Account(db_bind.Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    password = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))

    role = relationship("Role", uselist=False, back_populates="account")
    student = relationship("Student", back_populates="account")

    def change_password(self, new_password):
        self.password = new_password
        pass

    @staticmethod
    def generate_pass(n: int) -> str:
        return ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(n)))
