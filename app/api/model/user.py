""" User models """

import uuid

from werkzeug.security import generate_password_hash

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
    
    @property
    def password(self):
        raise AttributeError('Password: I only read but dont read.')
    
    