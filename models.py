from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(50))
    salary = db.Column(db.Float)
    holidays = db.Column(db.Integer)

    def __repr__(self):
        return f'<Employee {self.name}>'
