#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "BobHuang"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flask]'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN = "1161648480@qq.com"
    FLASK_POSTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = "1161648480@qq.com"
<<<<<<< HEAD
    MAIL_PASSWORD = "xmuudlzndryliedh"
=======
    MAIL_PASSWORD = "******"
>>>>>>> 5c0aad78bd3235e8d30598bf77bda717e6b9f9c5
    MAIL_PROT = 465
    MAIL_DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class TextingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TextingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

