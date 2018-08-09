# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/3/13 9:52'
from .models import Topics, Ask, AskAnswers, AnswersReply, Attachment
import xadmin


class TopicsAdmin(object):

    list_display = ['name', 'add_time', 'topic_ask_nums', ]
    search_fields = ['name', 'add_time', 'topic_ask_nums', ]
    list_filter = ['name', 'add_time', 'topic_ask_nums', ]

class AskAdmin(object):
    list_display = ['topics', 'user', 'title', 'detail', 'add_time', 'tag',]
    search_fields = ['topics', 'user', 'title', 'detail', 'add_time', 'tag',]
    list_filter = ['topics', 'user', 'title', 'detail', 'add_time', 'tag',]

class AskAnswersAdmin(object):
    list_display = ['user', 'ask', 'answer_title', 'answer_detail', 'add_time', ]
    search_fields = ['user', 'ask', 'answer_title', 'answer_detail', 'add_time', ]
    list_filter = ['user', 'ask', 'answer_title', 'answer_detail', 'add_time', ]

class AnswersReplyAdmin(object):
    list_display = ['user', 'ask', 'answer', 'answer_reply', 'add_time', ]
    search_fields = ['user', 'ask', 'answer', 'answer_reply', 'add_time', ]
    list_filter = ['user', 'ask', 'answer', 'answer_reply', 'add_time', ]


class AttachmentAdmin(object):
    list_display = ['img', 'file', 'video', 'ctime', 'mtime', ]
    search_fields = ['img', 'file', 'video', 'ctime', 'mtime', ]
    list_filter = ['img', 'file', 'video', 'ctime', 'mtime', ]


xadmin.site.register(Attachment, AttachmentAdmin)
xadmin.site.register(Topics, TopicsAdmin)
xadmin.site.register(Ask, AskAdmin)
xadmin.site.register(AskAnswers, AskAnswersAdmin)
xadmin.site.register(AnswersReply, AnswersReplyAdmin)