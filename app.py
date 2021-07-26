from flask import Flask, render_template, url_for





app = Flask(__name__)


@app.route("/")
def index():
    return render_template("root_layout.html")

@app.route("/auth/login")
def auth_login():
    return render_template("login.html")    

@app.route("/auth/signup")
def auth_signup():
    return render_template("signup.html")




