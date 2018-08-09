# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=8, choices=(('male', u'男'), ('female', u'女')),default='female')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    credit = models.IntegerField(verbose_name='积分', null=True)
    image = models.ImageField(upload_to='img/%Y/%m', default=u'image/default.png', max_length=100)
    register_time = models.DateField(verbose_name=u'注册时间', null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    #  不重载这个方法，实例化时不能大打印字符串
    def __unicode__(self):
        return self.username



class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(verbose_name=u'验证码类型',choices=(('registser', u'注册'), ('forget', u'找回密码'), ('update_email', u'修改邮箱')), max_length=30) # 开始max_length=10 update_email超了 无法验证
    send_time = models.DateTimeField(verbose_name=u'发送时间', default=datetime.now)# now去掉括号是实例化时的时间

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name

    # 重载Unicode方法
    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'站内消息'
        verbose_name_plural = verbose_name
    def __str__(self):
        # return self.user user是数字 会报错
        return self.message