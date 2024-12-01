from app import db

class OS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proprietary_name = db.Column(db.String(80), unique=False, nullable=False)
    number_fone = db.Column(db.Integer(15), nullable=False)
    device = db.Column(db.String(80), nullable=False)
    problem = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<OS %r>' % self.proprietary_name