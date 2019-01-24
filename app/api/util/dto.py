"""dto.py carries data between api calls """

from flask_restplus import Namespace, fields


class UserDto:
    """"
    User Data Transfer Object
    """
    api = Namespace('user', description='user related operations')
    user = api.model('user_details',{
        'user_name': fields.String(required=True, description="User's username"),
        'user_email': fields.String(required=True, description="User email address"),
        'password': fields.String(required=True, description="User password"),
        'user_uri': fields.String(description='User identifier')
    })
