from app.model.user import User

from app import response, db
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

import re

def createAdmin():
    try:
        # Validate mandatory fields and empty strings
        data = request.form
        if not all(field in data for field in ('name', 'email', 'password')):
            return response.badRequest([], "Missing mandatory fields: name, email, password")

        for field in ('name', 'email', 'password'):
            if data[field] == "" or data[field] is None:
                return response.badRequest([], f"Field '{field}' cannot be empty!")

        name = data['name'].strip()  # Remove leading/trailing whitespace
        email = data['email'].strip()
        password = data['password']
        level = 1

        # Validate email format
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            return response.badRequest([], "Invalid email format!")

        # Validate password length
        if len(password) < 8 or len(password) > 20:
            return response.badRequest([], "Password must be between 8 and 20 characters long!")

        # Check for existing email
        is_exist = User.query.filter(User.email == email).first()
        if is_exist is not None:
            return response.badRequest([], f"Data admin dengan email {is_exist.email} already exists!")

        # Create User object and set password securely
        user = User(name=name, email=email, level=level)
        user.setPassword(password)

        # Add user to database session and commit
        db.session.add(user)
        db.session.commit()

        return response.success("", "Sukses Menambahkan Data Admin!")
    except Exception as e:
        print(e)
        return response.internalServerError()
    
def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'level': data.level,
    }

    return data

def login():
    try:
        req = request.form
        email = req['email'].strip()
        password = req['password']

        # Validate email format
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            return response.badRequest([], "Invalid email format!")

        # Validate password length
        if len(password) < 8 or len(password) > 20:
            return response.badRequest([], "Password must be between 8 and 20 characters long!")

        user = User.query.filter(User.email == email).first()
        if not user:
            return response.badRequest([], "Email tidak terdaftar!")
        if not user.checkPassword(password):
            return response.badRequest([], "Kombinasi Password Salah!")
        
        data = singleObject(user)

        expires = timedelta(days=7)
        expires_refresh = timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
                "data": data,
                "access_token": access_token,
                "refresh_token": refresh_token,
        }, "Sukses Login!")


    except Exception as e:
        print(e)
        return response.internalServerError()
