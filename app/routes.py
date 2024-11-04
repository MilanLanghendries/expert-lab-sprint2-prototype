from flask import Blueprint, render_template, jsonify
import random

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/api/message")
def random_message():
    messages = [
        "Hello, welcome to our site!",
        "Enjoy exploring Flask with GitHub Actions!",
        "This is a random message from the server.",
    ]
    return jsonify({"message": random.choice(messages)})
