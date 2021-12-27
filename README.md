# PYTHON & SQL FINAL PROJECT

## ⚡ Infotech Employee Database

## 💡 Description

This project uses Object Relational Mapping (ORM) to create a database of employees for a fictionalcompany
named Infotech. It includes three entities which keeps track employee's personal information, labor category,
and contract they work on using One-To-One,One-to-Many, and Many-to-Many relationships. Additionally, the application
programming interface (API) that is included in the project, allows one to retrieve, modify , and delete records in every
table that is created in this project.

### 🤔 Retrospection

1. How did the projects design evolve over time?

My evolved from injecting raw SQL statements based off of my original ER digaram, to taking a more programmatic approch using
as I began understanding the later lessons of this course. I ultimately decided on reducing the number of attributes that were
originally associated with my entities, so I could more time fix bugs in ORM source code and getting it to compile without errors.

2. Did you choose to use an ORM or raw SQL? Why?

I decided to use an ORM because I get more practice using the Flask SQL Python Libraries that were taught in this course.

3. What future improvements are in store if any?

The future improvements of this program is as follows:

* Populating my association table.
* Incorporating visualization and indexing features.

### 📁 Core Files

* [seed.py](seed.py): Populates the tables in the *infotech* database.
* [models.py](infotech/src/models.py): Creates the tables in the *infotech* database.
* [table_data](infotech/src/table_data.py): Contains variables and functions needed to ingest data into the *infotech* database.
* [contract.py](infotech/src/api/contract.py): Contains the source code for the contract REST API framework.
* [employee.py](infotech/src/api/employee.py): Contains the source code for the employee REST API framework.
* [labor.py](infotech/src/api/labor.py): Contains the source code for the labor REST API framework.

### 📝 Table Design

**Labor_Categories Table:**

```python
class Labor(db.Model):
    __tablename__ = "labor_categories"
    id = db.Column(db.Integer, primary_key=True)
    labor_code = db.Column(db.String(5), unique=True,nullable=False)
    labor_category = db.Column(db.String(100),unique=True,nullable=False)
    salary = db.Column(db.Numeric(10,2), nullable=False)
    worker = db.relationship('Employee', backref='employee') # One-To Many Relationship
```

**Contracts_Table:**

```python
class Contract(db.Model):
    __tablename__ = "contracts"
    id = db.Column(db.Integer, primary_key=True)
    contract_name = db.Column(db.String(50),unique=True,nullable=False)
    customer_name = db.Column(db.String(50),nullable=False)
    open_reqs = db.Column(db.Integer, nullable=True)
    #labor = db.relationship('Labor', backref='labor')
    worker_id = db.relationship('Employee', backref='employee') # One to One Relationship
```

**Employees_Table:**

```python
class Employee(db.Model):
    __tablename__ = "employees"
        # Set autoincrement to user the SERIAL datatype
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    email_address = db.Column(db.String(50),unique=True,nullable=False)
    labor_id = db.Column(db.Integer,db.ForeignKey('labor_categories.id'), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False) # One-to-One-relationship
```

## 💡 REST API

### 📝 Contracts Table API Reference

**Contracts Table:**
| NAME   | METHOD     | ENDPOINT                                | DESCRIPTION                           |
|--------|------------|-----------------------------------------|---------------------------------------|
| delete | DELETE     | <http://localhost:5000/contract/><id:int> | Delete a contract object.             |
| create | POST       | <http://localhost:5000/contract/>         | Create a contract object.             |
| update | POST/PATCH | <http://localhost:5000/contract/><id:int> | Update a contract object.             |
| show   | GET        | <http://localhost:5000/contract/><id:int> | Show a contract object by contract id |
| index  | GET        | <http://localhost:5000/contract/>         | Show all contract objects.            |

**Contracts API Endpoint Requirements:**
**Create:** <http://localhost:5000/contract/>
 *Note:* Requires **all** of the following parameters

* contract_name (string)
* customer_name (string)
* open_reqs (integer)

**Update:** <http://localhost:5000/contract/><id:int>
 *Note:* Requires one or more of the following parameters

* contract_name (string)
* customer_name (string)
* open_reqs (integer)

### 📝 Employees Endpoint Table API Reference

**Employees Endpoints:**
| NAME   | METHOD     | ENDPOINT                                | DESCRIPTION                            |
|--------|------------|-----------------------------------------|----------------------------------------|
| delete | DELETE     | <http://localhost:5000/employee/><id:int> | Delete an employee object.             |
| create | POST       | <http://localhost:5000/employee/>         | Create an employee object.             |
| update | POST/PATCH | <http://localhost:5000/employee/><id:int> | Update an employee object.             |
| show   | GET        | <http://localhost:5000/employee/><id:int> | Show an employee object by employee.id |
| index  | GET        | <http://localhost:5000/employee/>         | Show all employee objects.             |

**Employees API Endpoint Requirements:**

**Create:** <http://localhost:5000/employee>
 *Note:* Requires **all** of the following parameters

* first_name (string)
* last_name (string)
* email_address (string)
* contract_id (integer)
* labor_id (integer)

**Update:** <http://localhost:5000/employee/><id:int>
 *Note:* Requires one or more of the following parameters

* first_name (string)
* last_name (string)
* email_address (string)
* contract_id (integer)
* labor_id (integer)

### 📝 Labor Categories Table API Reference

**Labor_Categories Endpoints:**
| NAME   | METHOD     | ENDPOINT                             | DESCRIPTION                                        |
|--------|------------|--------------------------------------|----------------------------------------------------|
| delete | DELETE     | <http://localhost:5000/labor/><id:int> | Delete a labor category object.                    |
| create | POST       | <http://localhost:5000/labor/>         | Create a labor category object.                    |
| update | POST/PATCH | <http://localhost:5000/labor/><id:int> | Update a labor category object.                    |
| show   | GET        | <http://localhost:5000/labor/><id:int> | Show a labor category object. by labor_category.id |
| index  | GET        | <http://localhost:5000/labor/>         | Show all labor category objects.                   |

**Labor_Categories API Endpoint Requirements:**

**Create:** <http://localhost:5000/labor/>
 *Note:* Requires **all** of the following parameters

* labor_category (string)
* labor_code (varchar(5))
* salary (float(10,1) ex. 100000.0)

**Update:** <http://localhost:5000/labor/><id:int>
 *Note:* Requires one or more of the following parameters

* labor_category (string)
* labor_code (varchar(5))
* salary (float(10,1) ex. 100000.0)
