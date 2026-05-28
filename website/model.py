from . import Db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Account(Db.Model, UserMixin):
    account_number=Db.column(Db.integer, primary_key=True)
    account_holder_name=Db.column(Db.string(150), nullable=False)
    password=Db.column(Db.string(150), nullable=False)
    account_details=Db.relationship("account_details", backref="customer")

class Account_details(Db.Model):
    account_number=Db.column(Db.integer, primary_key=True)
    balance=Db.column(Db.integer, nullable=False, default=0)
    loan=Db.column(Db.integer, nullable=False, default=0)
    bills_due=Db.column(Db.integer, nullable=False, default=0)