# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/3/13 11:06'
from django.contrib import admin
from django.conf.urls import url, include
from .views import AskListView, AskAnswersView, PostView, AddAnswerView, AddReplyView
import xadmin


urlpatterns = [

    url('list/(?P<topic_id>.*)$', AskListView.as_view(), name='chushilist'),
    url('ask/(?P<ask_id>.*)$', AskAnswersView.as_view(), name='chushiask'),
    url('po/(?P<topic_id>.*)$',PostView.as_view(), name='post'),
    url('add_answer/(?P<ask_id>.*)$', AddAnswerView.as_view(), name='Add_answer'),
    url('add_reply/(?P<answer_id>.*)$', AddReplyView.as_view(), name='add_reply'),

]