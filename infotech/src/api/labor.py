#!/usr/bin/python3
import re
from flask import Blueprint, json, jsonify, abort, request
from ..models import Labor, Contract, Employee,db
from decimal import Decimal

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Decimal): return float(obj)

bp = Blueprint('labor_categories', __name__, url_prefix='/labor')
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs.
def index():
    labor_cats = Labor.query.all() # ORM performs SELECT query
    result = []
    for cat in labor_cats:
        result.append(cat.serialize())
    return json.dumps(result, cls=Encoder)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    labor_cat = Labor.query.get_or_404(id)
    return json.dumps(labor_cat.serialize(), cls=Encoder) # Return JSON response

@bp.route('', methods=['POST'])
def create():
    if 'labor_category' not in request.json or 'labor_code' not in request.json or 'salary' not in request.json:
        return abort(400)
    labor_category = request.json['labor_category']
    labor_code = request.json['labor_code']
    salary = request.json['salary']
    labor_cat = Labor(
        labor_category=labor_category,
        labor_code=labor_code,
        salary=salary
    )
    db.session.add(labor_cat)
    db.session.commit()
    return json.dumps(labor_cat.serialize(), cls=Encoder)

@bp.route('/<int:id>', methods=['PATCH', 'PATCH'])
def update(id:int):
    labor_cat = Labor.query.get_or_404(id)
    if 'labor_category' not in request.json and 'labor_code' not in request.json and 'salary' not in request.json:
        return jsonify(False)

    if 'labor_category' in request.json:
        labor_category = request.json['labor_category']
    if 'labor_code' in request.json:
        labor_code = request.json['labor_code']
    if 'salary' in request.json:
        salary = request.json['salary']

    for key in request.json.keys():
        if key == 'labor_code':
            labor_cat.labor_code = labor_code
        elif key == 'labor_category':
            labor_cat.labor_category = labor_category
        elif key == 'salary':
            labor_cat.salary = salary
    db.session.commit()
    return json.dumps(labor_cat.serialize(), cls=Encoder)

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    labor_cat = Labor.query.get_or_404(id)
    try:
        db.session.delete(labor_cat) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)