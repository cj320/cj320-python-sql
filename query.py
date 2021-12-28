#!/usr/bin/python3
from faker import Faker
from infotech.src.models import Labor, Contract, Employee, association_table, db
from infotech.src.table_data import create_employees, contracts, labor_categories
from infotech.src import create_app
from pprint import pformat

app = create_app()
app.app_context().push()
results = db.session.query(Employee,Labor,Contract). \
    select_from(Employee).join(Labor).join(Contract).all()

data = []
for e, l,c in results:
    d = {
            "first name": e.first_name,
            "last name": e.last_name,
            "labor_category": l.labor_category,
            "salary": l.salary,
            "contract name": c.contract_name,
            "customer_name": c.customer_name,
        }
    data.append(d)
print(pformat(data))