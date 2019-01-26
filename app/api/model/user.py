""" User models """

import uuid

from passlib.hash import pbkdf2_sha256 as sha256
from app.api.db.mock_db import MockDB


class User:
    """
    User model class
    """
    def __init__(self, user_name, user_email, password):
        """ Instantiates the user class """
        self.user_id = str(uuid.uuid4())
        self.user_name = user_name
        self.user_email = user_email
        self.password = password

    def display_user_holder(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_email': self.user_email,
            'password': self.password
        }

    @classmethod
    def generate_password_hash(cls, password):
        """ Method to encrypt password """
        return sha256.hash(password)

    @classmethod
    def verify_hash_password(cls, password, hash):
        """  Method to decrypt password """
        return sha256.verify(password, hash)

    @classmethod
    def get_user_by_username(cls, user_name):
        """Method to get a user in the USER list by username"""
        for user in MockDB.USERS:
            user = user.display_user_holder()
            if user["user_name"] == user_name:
                return user

    @classmethod
    def get_user_by_email(cls, user_email):
        """ Method to get a user in the USER lIST by email """
        for user in MockDB.USERS:
            user = user.display_user_holder()
            if user["user_email"] == user_email:
                return user
