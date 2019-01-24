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
