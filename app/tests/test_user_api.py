""" Tests for user api """

from .base_test import BaseTestData
import json


class UserAPITestCase(BaseTestData):
    """
    Class testing user api which inherits from the BaseTestData class
    """

    def test_api_can_create_new_user(self):
        """
        Test api return success message on success registration
        : return STATUS CODE 201 OK Created
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.user_holder
        )
        json_data = response.get_json()
        self.assertTrue(json_data["message"] == "Successfully registered!")
        self.assertEqual(response.status_code, 201)

    def test_api_cannot_register_duplicate_user(self):
        """
        Test api returns error message on attempt to register user
        with same details again
        :return STATUS CODE 409 Conflict
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.user_holder
        )
        self.assertEqual(response.status_code, 201)
        response_2 = self.client.post(
            '/api/v1/users',
            json=self.user_holder
        )
        self.assertEqual(response_2.status_code, 409)


    def test_api_return_error_null_username(self):
        """
        Test api returns correct error code on attempt to register
        user with no username
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.null_username_holder
        )
        self.assertEqual(response.status_code, 400)

    def test_api_return_error_null_password(self):
        """
        Test api returns correct error code on attempt to register
        user with no password
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.null_password_holder
        )
        self.assertEqual(response.status_code, 400)

    def test_api_return_error_malformed_email(self):
        """
        Test api returns correct error code on attempt to register
        user with an invalid email format
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.malformed_email_holder
        )
        self.assertEqual(response.status_code, 400)

    def test_api_return_error_null_email(self):
        """
        Test api returns correct error code on attempt to register
        user with no email provided
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.null_email_holder
        )
        self.assertEqual(response.status_code, 400)

    def test_api_return_error_null_user_entries(self):
        """
        Test api returns correct error code on attempt to register
        user with empty username, email and password fields
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.null_user_entries_holder
        )
        self.assertEqual(response.status_code, 400)

    def test_api_return_error_int_user_name(self):
        """
        Test api returns correct error code on attempt to register
        user with numbers as username
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.int_username_holder
        )
        self.assertEqual(response.status_code, 400)

    def test_api_return_error_invalid_password_length(self):
        """
        Test api returns correct error code on attempt to register
        user with empty username, email and password fields
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.password_length_holder
        )
        self.assertEqual(response.status_code, 400)
