"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(50), default="/static/icon_default.jpg")
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default = func.now())
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    creator = db.relationship("User", backref="posts")