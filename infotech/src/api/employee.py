#!/usr/bin/python
from flask import Blueprint, json, jsonify, abort, request
from ..models import Employee,db
from decimal import Decimal

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Decimal): return float(obj)

bp = Blueprint('employees', __name__, url_prefix='/employee')
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs.
def index():
    employees = Employee.query.all() # ORM performs SELECT query
    result = []
    for employee in employees:
        result.append(employee.serialize())
    return jsonify(result) # Return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    employee = Employee.query.get_or_404(id)
    return json.dumps(employee.serialize(), cls=Encoder) # Return JSON response

@bp.route('', methods=['POST'])
def create():
    keys = [
        'first_name',
        'last_name',
        'email_address',
        'labor_id',
        'contract_id'
    ]
    for key in keys:
        if key not in request.json:
            return abort(400)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email_address = request.json['email_address']
    labor_id = request.json['labor_id']
    contract_id = request.json['contract_id']
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        email_address=email_address,
        contract_id=contract_id,
        labor_id=labor_id,
    )
    db.session.add(employee)
    db.session.commit()
    return json.dumps(employee.serialize(), cls=Encoder)

@bp.route('/<int:id>', methods=['PATCH', 'PATCH'])
def update(id:int):
    employee = Employee.query.get_or_404(id)
    if (
        'first_name' not in request.json
        and 'last_name' not in request.json
        and 'email_address' not in request.json
        and 'contract_id' not in request.json
        and 'labor_id' not in request.json
        ):
            return jsonify(False)
    if 'first_name' in request.json:
        first_name = request.json['first_name']
    if 'last_name' in request.json:
        last_name = request.json['last_name']
    if 'email_address' in request.json:
        email_address = request.json['email_address']
    if 'contract_id' in request.json:
        contract_id = request.json['contract_id']
    if 'labor_id' in request.json:
        labor_id = request.json['labor_id']

    for key in request.json.keys():
        if key == 'first_name':
            employee.first_name = first_name
        if key == 'last_name':
            employee.last_name = last_name
        if key == 'email_address':
            employee.email_address = email_address
        if key == 'contract_id':
            employee.contract_id = contract_id
        if key == 'labor_id':
            employee.labor_id = labor_id
    db.session.commit()
    return json.dumps(employee.serialize(), cls=Encoder)

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    employee = Employee.query.get_or_404(id)
    try:
        db.session.delete(employee) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

