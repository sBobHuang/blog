#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

#设置验证函数
login_manage = LoginManager()
login_manage.session_protection = 'strong'
login_manage.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #使用默认的flask配置

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manage.init_app(app)
    pagedown.init_app(app)
    #配置各个实例对象

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #倒入蓝图

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
