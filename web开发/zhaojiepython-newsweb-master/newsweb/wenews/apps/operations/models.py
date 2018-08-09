# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from users.models import UserProfile
from news.models import News, NewsTopic



class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机')
    news_name = models.CharField(max_length=50, verbose_name=u'新闻专题名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户提交'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class NewsComments(models.Model):
    '课程评论'
    user = models.ForeignKey(UserProfile, verbose_name=u'用户名')
    news = models.ForeignKey(News, verbose_name=u'新闻')
    comments = models.CharField(max_length=200, verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
       verbose_name = u'新闻评论'
       verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=((1, '新闻'), ), default=1, verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username

class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name
    def __str__(self):
        # return self.user user是数字 会报错
        return self.message

class UserNewsTopic(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    news = models.ForeignKey(NewsTopic, verbose_name=u'新闻')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户新闻'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username
