from flask import request, jsonify
from sqlalchemy import asc, desc

from app import app
from app import db
from model import client
from model.client import Client


@app.route("/client", methods=["POST"])
def register_client():
    data = request.get_json()
    new_client = Client(username=data['username'],
                        number_fone=data['number_fone'],
                        email=data['email'])
    db.session.add(new_client)
    db.session.commit()

    return jsonify({'id': client.id, 'username': client.username, 'email': client.email, 'number_fone': client.number_fone}), 201