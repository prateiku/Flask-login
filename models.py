from email.policy import default
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)
    data = db.Column(db.String(200), nullable=False, default="dp3.jpg")
    description = db.Column(db.String(1200), nullable=False, default="No description")

    def __repr__(self):
        return '<User %r>' % self.username