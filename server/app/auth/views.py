from flask import request
from . import app

@app.route("/login", methods=['POST'])
def login():    
    email = request.form.get("email")
    password = request.form.get("password")