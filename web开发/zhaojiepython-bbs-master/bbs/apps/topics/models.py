# coding=utf-8
from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.
class Topics(models.Model):
    name = models.CharField(max_length=30, default='话题', verbose_name='话题名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    topic_ask_nums = models.IntegerField( default=0, verbose_name='话题问答数量')

    class Meta:
        verbose_name = u'话题'
        verbose_name_plural  = verbose_name

    def __str__(self):
        return self.name

class Ask(models.Model):
    topics = models.ForeignKey(Topics, verbose_name='所属话题', null=True)
    user = models.ForeignKey(UserProfile, verbose_name='用户名' ,null=True)
    title = models.CharField(max_length=50, verbose_name='问题')
    detail = models.TextField(max_length=500, verbose_name='问题细节')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    tag = models.CharField(max_length=10, verbose_name='标签', default='经验总结')

    class Meta:
        verbose_name = u'问题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class AskAnswers(models.Model):
    '问题回答'
    user = models.ForeignKey(UserProfile, verbose_name=u'用户名')
    ask = models.ForeignKey(Ask, verbose_name=u'问题', null=True)
    answer_title = models.CharField(max_length=200, verbose_name=u'回答')
    answer_detail = models.TextField(max_length=500, verbose_name='详细回答', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
       verbose_name = u'问题回答'
       verbose_name_plural = verbose_name
    def __str__(self):
        return self.answer_detail


class AnswersReply(models.Model):
    '课程评论'
    user = models.ForeignKey(UserProfile, verbose_name=u'用户名')
    ask = models.ForeignKey(Ask, verbose_name=u'课程', null=True)
    answer = models.ForeignKey(AskAnswers, verbose_name=u'回答', null=True)
    answer_reply = models.TextField(max_length=200, verbose_name='回复',default='', null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
       verbose_name = u'回答回复'
       verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username


class Attachment(models.Model):
    """
    附件数据库，图片地址，文件地址和视频地址，在content内容里关联
    """
    img = models.ImageField(upload_to='img', default='')
    file = models.FileField(upload_to='file', default='')
    video = models.FileField(upload_to='video', default='')
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'附件上传'
        verbose_name_plural = verbose_name


