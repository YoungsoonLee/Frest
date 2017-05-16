# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app.modules import frest
from app import db
from app.models.user_model import UserModel, email_confirmed
from app.modules.frest.serialize.user import serialize_user
from app.models.user_token_model import token_generate

_URL = '/confirm'


class Confirm(Resource):

    """
    @api {post} /confirm email with email token
    @apiName EmailConfirm
    @apiGroup Cofirm

    @apiParam {String} token Users' email token.
    @apiParam {String} id Users' id.

    @apiSuccess (200) {String} this token is already pass the condition of token.
    @apiError (400) 
    """

    @frest.API
    def post(self):
        token = request.form.get('token', None)
        id = request.form.get('id', None) # !!!

        user = email_confirmed(id)

        if user is not None:
            _return = {
                'data': token_generate(email=user.email)
            }
            return _return, status.HTTP_200_OK
        else:
            return None, status.HTTP_400_BAD_REQUEST

        """
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
