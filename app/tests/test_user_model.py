# test user model

import unittest
import uuid

from app.api.model.user import User
from app.api.db.mock_db import MockDB
from app.api.service.user import save_new_user, save_changes


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
    
    def test_user_object_creation(self):
        """ 
        test user object is initialized properly
        """
        self.assertTrue(self.new_user.user_id)
        self.assertEqual(self.new_user.user_name, 'anonymous')
        self.assertEqual(self.new_user.user_email, 'anonymous@anony.com')
        self.assertEqual(self.new_user.password, 'password')
    
    def test_user_is_saved(self):
        """ Test user is saved on USERS list """
        save_changes(self.new_user)
        self.assertEqual(len(MockDB.USERS), 1)
    
    def test_multple_users_are_saved(self):
        """ Test multiple users are saved in USERS list"""
        save_changes(self.new_user)
        test_user = User('anonymous2', 'anonymous2@gmail.com', 'password')
        save_changes(test_user)
        self.assertEqual(len(MockDB.USERS), 2)



