#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登陆')

class RegistrationForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    username = StringField('账号', validators=[Required(), Length(1, 64)])
    password = PasswordField('密码', validators=[Required(),EqualTo('password2',message='两次输入的密码不一样！')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('账户已注册')

