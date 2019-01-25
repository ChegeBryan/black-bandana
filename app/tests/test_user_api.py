""" Tests for user api """

from .base_test import BaseTestData



class UserAPITestCase(BaseTestData):
    """
    Class testing user api which inherits from the BaseTestData class
    """

    def test_api_can_create_new_user(self):
        """
        use the test_client
        : return STATUS CODE 201 OK Created
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/users',
            json=self.user_holder
        )
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

