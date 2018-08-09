# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/3/6 21:19'
from .models import NewsTopic, News, Video
import xadmin


class NewsTopicAdmin(object):
    list_display = ['topic_name', 'desc',  'category', 'user_nums', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['topic_name', 'desc',  'category',  'user_nums', 'fav_nums', 'image', 'click_nums']
    list_filter = ['topic_name', 'desc', 'category',  'user_nums', 'fav_nums', 'image', 'click_nums','add_time']


class NewsAdmin(object):
    list_display = ['news_topic', 'title', 'add_time']
    search_fields =['news_topic', 'title', 'add_time']
    list_filter = ['news_topic__topic_name', 'title', 'add_time']

class VideoAdmin(object):
    list_display = ['news', 'name', 'add_time', 'watchtime']
    search_fields = ['news', 'name', 'add_time', 'watchtime']
    list_filter = ['news__title', 'name', 'add_time', 'watchtime']

xadmin.site.register(NewsTopic, NewsTopicAdmin)
xadmin.site.register(News, NewsAdmin)
xadmin.site.register(Video, VideoAdmin)

