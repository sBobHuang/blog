#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import traceback
from flask import current_app, render_template
from flask_mail import Message
from threading import Thread

def send_async_email(app, msg,subject,to):
    #发送邮件
    with app.app_context():
        #调用上下文
        fromaddr = "1161648480@qq.com"
<<<<<<< HEAD
        password = "sqientgvtwomjjfi"
=======
        password = "***"
>>>>>>> 5c0aad78bd3235e8d30598bf77bda717e6b9f9c5
        try:
            s = smtplib.SMTP_SSL()
            s.connect("smtp.qq.com", 465)  # 连接smtp服务器
            s.login(fromaddr, password)  # 登录邮箱
            s.sendmail(fromaddr, to, msg.as_string())  # 发送邮件
            s.quit()
        except Exception, e:
            print "Error: unable to send email"
            print traceback.format_exc()

def send_emial(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    #使用工厂函数调用app
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = render_template(template + '.html', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg,subject,[to]])
    thr.start()
    return thr
