from application import app
from flask import render_template


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # try the if login function in index file
    return render_template("index.html", login=False)

@app.route("/login")
def login():
    # try the if login function in index file
    return render_template("login.html", login=False)

@app.route("/courses")
def courses():
    # try the if login function in index file
    return render_template("courses.html", login=False)

@app.route("/register")
def register():
    # try the if login function in index file
    return render_template("register.html", login=False)
