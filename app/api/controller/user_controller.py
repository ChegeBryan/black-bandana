""" User api endpoints """

from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user import save_new_user


api = UserDto.api
_user = UserDto.user


@api.route('/users')
class Users(Resource):
    """
    User resource for the API
    """
    @api.doc('Create a new user')
    @api.expect(_user, validate=True)
    @api.response(201, 'Successfully registered user')
    def post(self):
        """ Create new user post method """
        data = request.get_json()
        return save_new_user(data=data)

