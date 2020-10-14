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
    MAIL_PASSWORD = "xmuudlzndryliedh"
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

