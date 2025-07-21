from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CaseSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    case_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
