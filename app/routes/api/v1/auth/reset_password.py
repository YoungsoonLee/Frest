# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app.modules import frest
from app.models.user_model import UserModel, get_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
from app import db
from app.modules.auth.login import verify_password

# add youngtip
from json import loads, dumps


_URL = '/auth/reset_password'


class ResetPassword(Resource):

    """
    @api {post} /auth/reset_password reset password
    @apiName 
    @apiGroup 

    @apiParam {String} email Users' email.

    @apiSuccess (200) 
    @apiError (400) 
    """

    @frest.API
    def post(self):
        email = request.form.get('email', None)
        new_password = request.form.get('new_password', None)

        # check email
        user = UserModel.query.filter(UserModel.email == email).first()
        # if okay, resset
        if user is None:
            _return = {
                'message': 'Email does not exist.',
                'field': 'Email'
            }

            return _return, status.HTTP_400_BAD_REQUEST
        else:
            #reset password
            try:
                user.password = generate_password_hash(new_password)
                db.session.commit()

            except IntegrityError as e:
                field, value = get_exists_error(e)

                _return = {
                    'message': "'" + value + "' is error.",
                    'field': getattr(form, field).label.text
                }

                return _return, status.HTTP_400_BAD_REQUEST

            return None, status.HTTP_200_OK

    @frest.API
    def put(self):
        email = request.form.get('email', None)
        old_password = request.form.get('old_password', None)
        new_password = request.form.get('new_password', None)

        # check password with old_password
        if verify_password(email, old_password):
            #reset password
            user = UserModel.query.filter(UserModel.email == email).first()
            try:
                user.password = generate_password_hash(new_password)
                db.session.commit()

            except IntegrityError as e:
                field, value = get_exists_error(e)

                _return = {
                    'message': "'" + value + "' is error.",
                    'field': getattr(form, field).label.text
                }

                return _return, status.HTTP_400_BAD_REQUEST

            return None, status.HTTP_200_OK
        else:
            _return = {
                'message': 'User does not exist or the password does not match.'
            }
            return _return, status.HTTP_400_BAD_REQUEST

