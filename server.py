
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from linked_list import LinkedList
from hash_table import HashTable
from binary_search_tree import BinarySearchTree
from queue import Queue
from stack import Stack
import random

# app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_blog_posts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

db = SQLAlchemy(app)
now = datetime.now()

# models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    posts = db.relationship("BlogPost", cascade="all, delete")

class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# routes
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone = data["phone"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 200

@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all()  # by default, this method queries in ascending order
    all_users_list = LinkedList()

    for user in users:
        all_users_list.add_first({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })

    return jsonify(all_users_list.to_list()), 200

@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    users = User.query.all()  # by default, this method queries in ascending order
    all_users_list = LinkedList()

    for user in users:
        all_users_list.add({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })

    return jsonify(all_users_list.to_list()), 200

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    users = User.query.all()
    all_users_list = LinkedList()
    
    for user in users:
        all_users_list.add({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })
    
    user = all_users_list.get_user_by_id(user_id)
    return jsonify(user), 200

@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 200

@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "User does not exist"}), 400
    
    data = request.get_json()
    ht = HashTable(10)
    ht.add("title", data["title"])
    ht.add("body", data["body"])
    ht.add("date", now)
    ht.add("user_id", user_id)

    new_blog_post = BlogPost(
        title=ht.get_value("title"),
        body=ht.get_value("body"),
        date=ht.get_value("date"),
        user_id=ht.get_value("user_id")
    )

    db.session.add(new_blog_post)
    db.session.commit()

    return jsonify({"message": "New blog post created"}), 200

@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_blog_post(blog_post_id):
    blog_posts = BlogPost.query.all()
    random.shuffle(blog_posts)
    bst = BinarySearchTree()

    for post in blog_posts:
        bst.insert({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id
        })
    
    post = bst.search(int(blog_post_id))
    
    if not post:
        return jsonify({ "message": "post not found" })
    
    return jsonify(post), 200

@app.route("/blog_post/numeric_body", methods=["GET"])
def get_numeric_post_bodies():
    blog_posts = BlogPost.query.all()
    q = Queue()
    for post in blog_posts:
        q.enqueue(post)
    
    return_list = []
    
    while q and q.peek():
        post = q.dequeue()
        numeric_body = 0

        if post is None or post.data is None:
            print(q, post)

        for c in post.data.body:
            numeric_body += ord(c)
        
        post.data.body = numeric_body

        return_list.append({
            "id": post.data.id,
            "title": post.data.title,
            "body": post.data.body,
            "user_id": post.data.user_id,
        })
    
    return jsonify(return_list)

@app.route("/blog_post/delete_last_10", methods=["DELETE"])
def delete_last_10():
    blog_posts = BlogPost.query.all()
    s = Stack()

    for post in blog_posts:
        s.push(post)

    for _ in range(10):
        post_to_delete = s.pop().data
        db.session.delete(post_to_delete)
        db.session.commit()

    return jsonify({ "message": "success" })

if __name__ == "__main__":
    app.run(debug=True)
