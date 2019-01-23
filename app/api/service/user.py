""" Methods for data manipulation in the Mock db """

from app.api.db.mock_db import MockDB
from app.api.model.user import User


def save_new_user(data):
    """
    Save new user function 
    """
    username =  data['user_name']
    user_email = data['user_email']
    password = data['password']

    new_user = User(
        user_name=username,
        user_email=user_email,
        password=password
    )

    save_changes(new_user)


def save_changes(data):
    MockDB.USERS.append(data)