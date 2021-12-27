import random
from faker import Faker
EMPLOYEE_COUNT = 100

def create_employees():
    fake = Faker()
    employees = []
    for _ in range(EMPLOYEE_COUNT):
        first_name = fake.unique.first_name().capitalize()
        last_name = fake.unique.last_name().capitalize()
        email_address = first_name.lower() + '.' + last_name.lower() + str(random.randint(1,100)) + '@infotech.com'
        labor_id = random.randint(1,12)
        contract_id = random.randint(1,5)
        employee = {'first_name': first_name, 'last_name': last_name, 'email_address': email_address, 'labor_id':labor_id,
                    'contract_id':contract_id}
        employees.append(employee)
    return employees

# Contract Table Data
contracts = [
    {'contract_name': 'CRAFTYPANDA', 'customer_name': 'Baltimore Gas & Electric', 'open_reqs': 3},
    {'contract_name': 'SUNRISE', 'customer_name': 'Department of Energy', 'open_reqs': 20},
    {'contract_name': 'CODEELF', 'customer_name': 'Department of Defense', 'open_reqs': 0},
    {'contract_name': 'ARMORBYTE','customer_name': 'Montgomery County Police Department', 'open_reqs': 5},
    {'contract_name': 'STUDYHALL', 'customer_name': 'University of Maryland', 'open_reqs': 0}
]

# Labor Category Table Data
labor_categories = [
    {'labor_code': 'SA1', 'labor_category': 'System Administrator 1', 'salary': 50000.00},
    {'labor_code': 'SA2', 'labor_category': 'System Administrator 2', 'salary': 60000.00},
    {'labor_code': 'SA3', 'labor_category': 'System Administrator 3', 'salary': 70000.00},
    {'labor_code': 'SE1', 'labor_category': 'System Engineer 1', 'salary': 70000.00},
    {'labor_code': 'SE2', 'labor_category': 'System Engineer 2', 'salary': 90000.00},
    {'labor_code': 'SE3', 'labor_category': 'System Engineer 3', 'salary': 100000.00},
    {'labor_code': 'SIE1', 'labor_category': 'System Integration Engineer 1', 'salary': 80000.00},
    {'labor_code': 'SIE2', 'labor_category': 'System Integration Engineer 2', 'salary': 90000.00},
    {'labor_code': 'SIE3', 'labor_category': 'System Integration Engineer 3','salary': 100000.000},
    {'labor_code': 'DEV1', 'labor_category': 'Software Developer 1', 'salary': 100000.00},
    {'labor_code': 'DEV2', 'labor_category': 'Software Developer 2', 'salary': 150000.00},
    {'labor_code': 'DEV3', 'labor_category': 'Software Developer 3', 'salary': 200000.00}
]

