"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SHHHHH!"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()

@app.route("/")
def show_userlist():
    users = User.query.order_by(User.last_name).all()
    
    return render_template("list.html", users = users)

@app.route("/users/new")
def show_add_form():
    return render_template("add-user.html")

@app.route("/users/new", methods=["POST"])
def add_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    icon_url = request.form["icon_url"] if request.form["icon_url"] else None
    
    new_user = User(first_name = first_name, last_name = last_name, image_url = icon_url)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect("/")

@app.route("/users/<user_id>")
def show_user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user = user)

@app.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect("/")

@app.route("/users/<user_id>/edit")
def show_update_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("update-user.html", user=user)

@app.route("/users/<user_id>/edit", methods=["POST"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["icon_url"] if request.form["icon_url"] else None
    
    db.session.add(user)
    db.session.commit()
    
    return redirect(f"/users/{user.id}")