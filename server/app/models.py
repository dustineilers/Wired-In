from flask_sqlalchemy import SQLAlchemy, func

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_joined = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"User {self.username}"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    due_date = db.Column(db.DateTime(timezone=True), nullable=False)
    priority = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Task {self.name}"