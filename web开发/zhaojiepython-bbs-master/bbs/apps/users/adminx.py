# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/2/11 10:05'
import xadmin
from xadmin import views
from .models import UserProfile, EmailVerifyRecord, UserMessage
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '考研乱弹管理系统'
    site_footer = '考研论坛网'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type',]
    list_filter = ['code', 'email', 'send_type', 'send_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time', ]
    search_fields = ['user', 'message', 'has_read', ]
    list_filter = ['user', 'message', 'has_read', 'add_time', ]

xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)