# coding=utf-8
from django.db import models
from datetime import datetime

# Create your models here.


class NewsTopic(models.Model):
    topic_name = models.CharField(max_length=60, verbose_name='新闻专题')
    desc = models.CharField(max_length=300, verbose_name=u'新闻描述')
    detail = models.TextField(verbose_name=u'新闻详情')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否轮播')
    category = models.CharField(choices=(('ss', '时事'), ('dj', '财经'), ('gj', '国际')), max_length=2, verbose_name=u'新闻类别')

    user_nums = models.IntegerField(default=0, verbose_name=u'观看人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'封面图片', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    tag = models.CharField(default='', verbose_name=u'新闻标签', max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    news_annoucements = models.CharField(default='', max_length=500, verbose_name=u'公告')
    youneedknow = models.CharField(max_length=300, verbose_name=u'须知', default='')
    news_tell = models.CharField(max_length=300, verbose_name=u'我们告诉你', default='')
    class Meta:
        verbose_name = u'新闻专题'
        verbose_name_plural  = verbose_name

    def __str__(self):
        return self.topic_name

    def get_user(self):
        return self.usernewstopic_set.all()[:3]



class News(models.Model):
    news_topic = models.ForeignKey(NewsTopic, verbose_name=u'新闻')
    title = models.CharField(max_length=100, verbose_name=u'详细新闻名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title



class Video(models.Model):
    news = models.ForeignKey(News, verbose_name=u'详细新闻')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    url = models.CharField(max_length=200, default='', verbose_name=u'访问地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    watchtime = models.IntegerField(default=0, verbose_name=u'观看时长（分钟数）')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name