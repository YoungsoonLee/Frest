# -*- coding: utf-8 -*-
from flask import jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models.user_model import UserModel
from app.models.user_login_history_model import UserLoginHistoryModel


def verify_password(email, password):
    user = UserModel.query\
        .filter(UserModel.email == email)

    accepted = False

    if user.count() and password:
        accepted = check_password_hash(user.first().password, password)

        login_history = UserLoginHistoryModel(
            user_id=user.first().id,
            ip_address=request.remote_addr,
            agent=request.headers.get('User-Agent'),
            accepted=accepted
        )
        db.session.add(login_history)
        db.session.commit()

    return accepted

# return user
def verify_email(email):
    user_query = UserModel.query \
                .filter(UserModel.email == email)
    if user_query.count():
        return user_query.first()
    else:
        return None

