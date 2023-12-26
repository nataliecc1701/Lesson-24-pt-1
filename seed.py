from models import User, Post, db
from app import app

# need to do this in the current version of SQLAlchemy
app.app_context().push()

db.drop_all()
db.create_all()

users = [
    User(first_name = "Alan", last_name="Aida"),
    User(first_name = "Joel", last_name="Burton"),
    User(first_name = "Jane", last_name="Smith"),
    User(first_name = "Alyssa", last_name="Andersen"),
    User(first_name = "Samantha", last_name="Myers"),
]

posts = [
    Post(title="First Post!", content="w00t!", creator_id=2),
    Post(title="On Emptiness", content=" ", creator_id=4),
    
]

db.session.add_all(users)
db.session.commit()

db.session.add_all(posts)
db.session.commit()