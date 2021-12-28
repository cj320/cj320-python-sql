#!/usr/bin/python3
import datetime
from flask_sqlalchemy import SQLAlchemy
import simplejson as json
from decimal import Decimal


# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships
# Create a SQLAlchemy database adapter

db = SQLAlchemy()

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Decimal): return float(obj)

# Create the likes table which consists of a many to many relationship.
association_table = db.Table(
    'employee_to_contracts',
    db.Column(
        'employee_id', db.Integer,
        db.ForeignKey('employees.id'),
        primary_key=True
    ),
    db.Column(
        'contract_id', db.Integer,
        db.ForeignKey('contracts.id'),
        primary_key=True
    ),
    db.Column(
        'labor_id', db.Integer,
        db.ForeignKey('labor_categories.id'),
        primary_key=True
    )
)
class Employee(db.Model):
    __tablename__ = "employees"
        # Set autoincrement to user the SERIAL datatype
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    email_address = db.Column(db.String(50),unique=True,nullable=False)
    labor_id = db.Column(db.Integer,db.ForeignKey('labor_categories.id'), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
    contract = db.relationship("Contract", foreign_keys=[contract_id])
    labor_category = db.relationship("Labor", foreign_keys=[labor_id])

    def __init__(self,first_name:str,last_name:str,email_address:str,labor_id:int,contract_id:int):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.labor_id = labor_id
        self.contract_id = contract_id

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_address': self.email_address,
            'labor_id': self.labor_id,
            'contract_id': self.contract_id
        }



# Create the User class as a subclass of SQLAlchemy's db.Model
class Labor(db.Model):
    __tablename__ = "labor_categories"
    id = db.Column(db.Integer, primary_key=True)
    labor_code = db.Column(db.String(5), unique=True,nullable=False)
    labor_category = db.Column(db.String(100),unique=True,nullable=False)
    salary = db.Column(db.Numeric(10,2), nullable=False)
    employee_labor = db.relationship('Employee', backref='employee', lazy='dynamic')


    def __init__(self,labor_code:str,labor_category:str,salary:float):
        self.labor_code = labor_code
        self.labor_category = labor_category
        self.salary = salary

    def serialize(self):
        return {
            'id': self.id,
            'labor_code': self.labor_code,
            'labor_category': self.labor_category,
            'salary': self.salary
        }

class Contract(db.Model):
    __tablename__ = "contracts"
    id = db.Column(db.Integer, primary_key=True)
    contract_name = db.Column(db.String(50),unique=True,nullable=False)
    customer_name = db.Column(db.String(50),nullable=False)
    open_reqs = db.Column(db.Integer, nullable=True)
    workers = db.relationship('Employee', foreign_keys=[Employee.contract_id], backref='workers')

    def __init__(self,contract_name:str,customer_name:str,open_reqs:int):
        self.contract_name = contract_name
        self.customer_name = customer_name
        self.open_reqs = open_reqs

    def serialize(self):
        return {
            'id': self.id,
            'contract_name': self.contract_name,
            'customer_name': self.customer_name,
            'open_reqs': self.open_reqs
        }

