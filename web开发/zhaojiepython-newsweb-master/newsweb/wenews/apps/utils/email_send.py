# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/2/16 23:16'
from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from wenews.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '我们在线真心为您'
        email_body = '请点击下面的链接激活您的账号：http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '我们在线真心为您,重置密码'
        email_body = '请点击下面的链接重置您的密码：http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'update_email':
        email_title = '我们在线真心为您, 邮箱修改验证码'
        email_body = '请点击下面的链接修改你的邮箱：{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass