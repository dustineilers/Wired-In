from flask import request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import re
from . import auth

@auth.route("/login", methods=['POST'])
def login():    
    email = request.form.get("email")
    password = request.form.get("password")

    user = # query user from database

    if user: #check is user exists
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            return
        else:
            return {"msg": "Incorrect password"}, 401
    else:
        return {"msg": "Account with email does not exist"}, 401

@auth.route("/register", methods=['POST'])
def register():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password1")
    confirm_password = request.form.get("password2")

    email_exists = # query email from database
    username_exists  = # query username from database

    if email_exists:
        return {"msg": "Account with email already exists"}, 401
    elif username_exists:
        return {"msg": "Account with username already exists"}, 401
    elif password != confirm_password:
        return {"msg": "Passwords do not match"}, 401
    elif len(password) < 10:
        return {"msg": "Password is too short"}, 401
    elif not is_valid(email):
        return {"msg": "Email address is not valid"}, 401
    else:

    

@auth.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    return {"msg": "Logout successful"}

def is_valid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False