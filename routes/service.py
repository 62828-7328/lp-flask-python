from flask import request, jsonify
from sqlalchemy import asc, desc

from app import app
from app import db
from model import service
from model.service import Service

@app.route("/service", methods=["POST"])
def register_service():
    data = request.get_json()
    new_service = Service(service_type=data['service_type'],
                        price=data['price'])
    db.session.add(new_service)
    db.session.commit()

    return jsonify({'id': service.id, 'service_type': service.service_type, 'price': service.price}), 201

@app.route("/service", methods=["GET"])
def list_service():
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

    service = Service.query.filter_by(**filter).order_by(order_by).offset(offset).limit(limit).all()
    if not service:
        return jsonify([]), 200

    status_code = 206 if len(service) == limit else 200

    return jsonify({'id': service.id, 'service_type': service.service_type, 'price': service.price}), status_code