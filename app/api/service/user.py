""" Methods for data manipulation in the Mock db """

import re

from app.api.db.mock_db import MockDB
from app.api.model.user import User


def save_new_user(data):
    """
    Save new user function
    """
    username = data['user_name']
    user_email = data['user_email']
    password = data['password']

    # check if the data provided in the payload is valid
    # 1. Check if username, email, password is provided and return relevant errors on encounter with errors
    # 2. Check if the username, email, password are valid when provided
    if "user_name" in data and not data["user_name"].strip():
        return {
            'error': 'Username cannot be empty'
        }, 400
    elif "user_email" in data and not data["user_email"].strip():
        return {
            "error": "Email cannot be empty"
        }, 400
    elif "password" in data and not data["password"].strip():
        return {
            "error": "Password cannot be empty"
        }, 400
    # check if the username provided is numbers only
    elif username.isnumeric():
        return {
            "error": "Username cannot be a number"
        }, 400
    # check if the email provided follows email format
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', user_email):
        return {
            "error": "Invalid email format"
        }, 400
    elif not (8 <= len(password) <= 16):
        return {
            "error": "Password must be between 8 to 16 characters inclusive"
        }, 400
    else:
        # populate user variable if a user exists by that username or email
        # address
        username_found = User.get_user_by_username(username)
        user_email_found = User.get_user_by_email(user_email)

        # check if user exists before saving
        if username_found is None and user_email_found is None:
            new_user = User(
                user_name=username,
                user_email=user_email,
                password=User.generate_password_hash(password)
            )
            save_changes(new_user)
            response_object = {
                "message": "Successfully registered!",
                "user": new_user.display_user_holder()
            }
            return response_object, 201
        else:
            return {
                "error": "Try a different email and username combination",
            }, 409


def save_changes(data):
    MockDB.USERS.append(data)
