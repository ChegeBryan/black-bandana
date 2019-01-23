""" Methods for data manipulation in the Mock db """

from app.api.db.mock_db import MockDB


def save_new_user(data):
    """
    Save new user function 
    """
    pass

    

def save_changes(data):
    MockDB.USERS.append(data)