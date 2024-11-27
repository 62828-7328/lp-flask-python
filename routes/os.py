from flask import request, jsonify
from sqlalchemy import asc, desc

from app import app
from app import db
from model import os
from model.os import OS

@app.route("/os", methods=["POST"])
def register_os():
    data = request.get_json()
    new_os = OS(proprietary_name=data['proprietary_name'],
                        number_fone=data['number_fone'],
                        device=data['device'],
                        problem=data['problem'])
    db.session.add(new_os)
    db.session.commit()

    return jsonify({'id': os.id, 'proprietary_name': os.proprietary_name, 'number_fone': os.number_fone, 'device': os.device, 'problem': os.problem}), 201

@app.route("/os", methods=["GET"])
def list_os():
    query_params = request.args

    page = query_params.get('page', default=0, type=int)
    limit = query_params.get('limit', default=10, type=int)
    offset = page * limit

    filter = {}
    ignored_fields = ['page', 'limit', 'sort_by', 'sort_direction']
    for field, value in query_params.items():
        if field not in ignored_fields:
            filter[field] = value

    sort_by = query_params.get('sort_by', default='id', type=str)
    sort_direction = query_params.get('sort_direction', default='asc', type=str)

    order_by = asc(sort_by) if sort_direction == 'asc' else desc(sort_by)

    os = OS.query.filter_by(**filter).order_by(order_by).offset(offset).limit(limit).all()
    if not os:
        return jsonify([]), 200

    status_code = 206 if len(os) == limit else 200

    return jsonify({'id': os.id, 'proprietary_name': os.proprietary_name, 'number_fone': os.number_fone, 'device': os.device, 'problem': os.problem}), status_code