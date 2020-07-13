# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:18:09 2020

@author: jacob
"""
from threading import Thread

from flask_mail import Message, current_app
from app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()    