from app import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(40), unique=True, nullable=False)
    price = db.Column(db.Integer(15), nullable=False)

    def __repr__(self):
        return '<Service %r>' % self.service_type