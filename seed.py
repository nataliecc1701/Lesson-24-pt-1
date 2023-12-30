from models import User, Post, Tag, db
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

tags = [
    Tag(name="Introductions"),
    Tag(name="Life Updates"),
    Tag(name="Musings"),
    Tag(name="Poetry"),
    Tag(name="Fun"),
    Tag(name="Flask"),
    Tag(name="Programming"),
]

posts = [
    Post(title="First Post!", creator_id=2, content="w00t!",
         tags=[tags[0], tags[4]]),
    Post(title="On Emptiness", creator_id=4, content=" ",
         tags=[tags[2], tags[3]]),
    Post(title="The beginning", creator_id=1, content="I'm excited to share my blogging journey with all of you",
         tags=[tags[0], tags[1], tags[2]]),
    Post(title="Flask is great", creator_id=3, content="Flask is an amazing tool for creating websites",
         tags=[tags[5], tags[6]]),
    Post(title="Um, hi", creator_id=5, content="hello! or not! sorry for bothering you",
         tags=[tags[0]]),
    Post(title="What I had for breakfast today", creator_id=1, content="Hello dear subscribers! Today for breakfast I had an omelet. Stay tuned for more exciting updates",
         tags=[tags[4], tags[1]])
]

db.session.add_all(users)
db.session.commit()

db.session.add_all(tags)
db.session.commit()

db.session.add_all(posts)
db.session.commit()