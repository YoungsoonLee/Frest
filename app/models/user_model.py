# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    permission = Column(String(255), nullable=False, default='USER')
    confirmed = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)  # active or close
    is_anonymous = db.Column(db.Boolean, default=False) # guest or not (for future) 
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)
    closed_at = Column(DateTime)

    def __init__(self, username=None, email=None, password=None, permission=None, confirmed=None, is_active=None, is_anonymous=None):
        self.username = username
        self.email = email
        self.password = password
        self.permission = permission
        self.confirmed = confirmed
        self.is_active = is_active
        self.is_anonymous = is_anonymous   


def get_user(user_id=0):
    user_query = UserModel.query \
        .filter(UserModel.id == user_id).first()

    return user_query


def get_users(order='desc', page=0, limit=10):
    users = []

    users_query = UserModel.query \
        .order_by(UserModel.id.asc() if order == 'asc' else UserModel.id.desc()) \
        .limit(limit) \
        .offset(page * limit)

    for user in users_query:
        users.append(user)

    return users

def email_confirmed(id=None):
    user = get_user(id)
    
    if user is not None:
        user.confirmed = True
        db.session.commit()
        # return True
        return user
    else:
        return None

def verify_email(email):
    user_query = UserModel.query \
        .filter(UserModel.email == email).first()
    return user_query
    

