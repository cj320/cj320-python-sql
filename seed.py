import random
import string
import hashlib
import secrets
from faker import Faker
from infotech.src.models import Labor, Contract, Employee, association_table, db
from infotech.src.table_data import create_employees, contracts, labor_categories
from infotech.src import create_app

def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(association_table.delete())
    Labor.query.delete()
    Contract.query.delete()
    Employee.query.delete()
    db.session.commit()

def main():
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()

    # Insert data into Labor Category Table
    for labor_cat in labor_categories:
        infotech_labor_cat = Labor(**labor_cat)
        db.session.add(infotech_labor_cat)
        db.session.commit()

    # Insert Data into Contracts Table
    for contract in contracts:
        infotech_contract = Contract(**contract)
        db.session.add(infotech_contract)
        db.session.commit()

    # Insert Employees into Employees Table
    infotech_employees = create_employees()
    for employee in infotech_employees:
        infotech_employee = Employee(**employee)
        db.session.add(infotech_employee)
        db.session.commit()

if __name__ == "__main__":
    main()