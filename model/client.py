from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    number_fone = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Client %r>' % self.username