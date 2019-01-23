""" Data that wil be used on tests for on api for users """

import unittest

from app import create_app


class BaseTestData(unittest.TestCase):
    """
    Test data base class
    """
    def setUp(self):
        """ Initialize app and the test data """
        self.app = create_app('testing')
