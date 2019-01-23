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

        self.user = User(user_name='name', user_email='anonymous@gmail.com', password='password23')
        self.user_holder = self.user.display_user_holder()
        self.null_username = User(user_name='', user_email='anonymous@gmail.com', password='password')
        self.null_username_holder = self.null_username.display_user_holder()
        self.malformed_email = User(user_name='name', user_email='anoy.com', password='password21')
        self.malformed_email_holder = self.malformed_email.display_user_holder()
        self.null_password = User(user_name='name', user_email='anonymous@gma.com', password='')
        self.null_password_holder = self.null_password.display_user_holder()
        self.null_user_entries = User(user_name='', user_email='', password='')
        self.null_user_entries_holder = self.null_user_entries.display_user_holder()
        self.int_username = User(user_name=3222, user_email='anonymous@gam.com', password='password23')
        self.int_username_holder = self.int_username.display_user_holder()
        self.password_length = User(user_name='name', user_email='anonymous@gm.com', password='passw')
        self.password_length_holder = self.password_length.display_user_holder()

