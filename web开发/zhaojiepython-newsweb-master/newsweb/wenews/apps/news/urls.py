# -*- coding=utf-8 -*-
from django.conf.urls import url
from .views import NewsTopicListView, NewsDetailView, AddFavView
__author__ = 'zhaojie'
__date__ = '2018/3/6 18:13'

urlpatterns = [

    url(r'topiclist/$', NewsTopicListView.as_view(), name='topiclist'),
    url(r'detail/(?P<topic_id>\d+)$',NewsDetailView.as_view(), name='detail'),
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),

]