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