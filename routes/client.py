from flask import request, jsonify
from sqlalchemy import asc, desc

from app import app
from model.client import Client


@app.route("/client", methods=["POST"])
def list_client():
    query_params = request.args
    new_client = Client(username=data['username'],
                        number_fone=data['number_fone'],
                        email=data['email'])

    return jsonify(result), status_code