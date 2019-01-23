""" Data that wil be used on tests for on api for users """

import unittest

from app import create_app
from app.api.model.user import User


class BaseTestData(unittest.TestCase):
    """
    Test data base class
    """
    def setUp(self):
        """ Initialize app and the test data """
        self.app = create_app('testing')

        self.user = User(user_name='name', user_email='anonymous@gmail.com', password='password')
        self.user_holder = self.user.display_user_holder()
        self.null_username = User(user_name='', user_email='anonymous@gmail.com', password='password')
        self.null_username_holder = self.null_username.display_user_holder()
        

