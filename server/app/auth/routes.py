from flask import request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth

@auth.route("/login", methods=['POST'])
def login():    
    email = request.form.get("email")
    password = request.form.get("password")

@auth.route("/register", methods=['POST'])
def register():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password1")
    confirm_password = request.form.get("password2")

@auth.route("/logout")
@login_required
def logout():
    logout_user()