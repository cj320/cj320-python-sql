#!/usr/bin/python3
from flask import Blueprint, json, jsonify, abort, request
from ..models import Contract,db
from decimal import Decimal

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Decimal): return float(obj)

bp = Blueprint('contracts', __name__, url_prefix='/contract')
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs.
def index():
    contracts = Contract.query.all() # ORM performs SELECT query
    result = []
    for contract in contracts:
        result.append(contract.serialize())
    return jsonify(result) # Return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id:int):
    result = Contract.query.get_or_404(id)
    return json.dumps(result.serialize(), cls =Encoder) # Return JSON response


@bp.route('', methods=['POST'])
def create():
    if 'contract_name' not in request.json or 'customer_name' not in request.json or 'open_reqs' not in request.json:
        return abort(400)
    contract_name = request.json['contract_name']
    customer_name = request.json['customer_name']
    open_reqs = request.json['open_reqs']
    contract = Contract(
        contract_name=contract_name,
        customer_name=customer_name,
        open_reqs=open_reqs
    )
    db.session.add(contract)
    db.session.commit()
    return json.dumps(contract.serialize(), cls=Encoder)

@bp.route('/<int:id>', methods=['PATCH', 'PATCH'])
def update(id:int):
    contract = Contract.query.get_or_404(id)
    if 'contract_name' not in request.json and 'customer_name' not in request.json and 'open_reqs' not in request.json:
        return jsonify(False)

    if 'contract_name' in request.json:
        contract_name = request.json['contract_name']
    if 'customer_name' in request.json:
        customer_name = request.json['customer_name']
    if 'open_reqs' in request.json:
        open_reqs = request.json['open_reqs']

    for key in request.json.keys():
        if key == 'contract_name':
            contract.contract_name = contract_name
        elif key == 'customer_name':
            contract.customer_name = customer_name
        elif key == 'open_reqs':
            contract.open_reqs = open_reqs
    db.session.commit()
    return json.dumps(contract.serialize(), cls=Encoder)

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    contract = Contract.query.get_or_404(id)
    try:
        db.session.delete(contract) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

