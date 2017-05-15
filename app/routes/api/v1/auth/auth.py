# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app.models.user_token_model import token_generate
from app.modules import frest
from app.modules.auth.login import verify_password, verify_email
from app.modules.frest.serialize.user import serialize_user

# add youngtip
from json import loads, dumps


_URL = '/auth'


class Auth(Resource):

    """
    @api {post} /auth Authenticate with user information. (login)
    @apiName UserAuth
    @apiGroup Auth

    @apiParam {String} email Users' email.
    @apiParam {String} password Users' password.

    @apiSuccess (200) {String} data Generated JWT token.
    @apiError (400) AuthFail User does not exist or the password does not match
    """

    @frest.API
    def post(self):
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        if verify_password(email, password):
            # add youngtip
            # check confirmed
            _return = {
                'data': token_generate(email=email)
            }
            return _return, status.HTTP_200_OK
        else:
            _return = {
                'message': 'User does not exist or the password does not match.'
            }
            return _return, status.HTTP_400_BAD_REQUEST

    """
    @api {put} /auth reset-password
    @apiName UserAuth
    @apiGroup Auth

    @apiParam {String} email Users' email.

    @apiSuccess (200) {String} data Generated JWT token.
    @apiError (400) AuthFail User does not exist or the password does not match
    """
    @frest.API
    def put(self):
        email = request.form.get('email', None)
        user = verify_email(email)

        if  user is not None:
            _return = {
                'data': serialize_user(user)
            }
            return _return, status.HTTP_200_OK
        else:
            _return = {
                'message': 'User does not exist.'
            }
            return _return, status.HTTP_400_BAD_REQUEST


