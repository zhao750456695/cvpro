# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/3/7 16:37'
from django.conf.urls import url, include
from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyTopicView,  FavCourseView, MyMessageView
urlpatterns =[
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),
    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    # 用户修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    # 发送邮箱验证码
    url(r'sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),
    # 修改邮箱
    url(r'^update_email/$',UpdateEmailView.as_view(), name='update_email'),
    # 我的课程
    url(r'^mytopic/$',MyTopicView.as_view(), name='mycourse'),

    url(r'^myfav/course/$', FavCourseView.as_view(), name='myfav_course'),
    url(r'^mymessage/$', MyMessageView.as_view(), name='mymessage'),

]