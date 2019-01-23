# test user model

import unittest
import uuid

from app.api.model.user import User


class TestUserModel(unittest.TestCase):
    """ Test class for user maodel class """
    def setUp(self):
        """
        Creation of user object
        :arg: user_id, username, useremail, password 
        :return: user object
        """
        __id = str(uuid.uuid4())
        self.new_user = User(
            'anonymous',
            'anonymous@anony.com',
            'password'
        )

