# -*- coding=utf-8 -*_
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
    image = models.ImageField(upload_to='img/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    #  不重载这个方法，实例化时不能大打印字符串
    def __str__(self):
        return self.username

    def unread_nums(self):
        # 获得用户未读信息的数量
        from operations.models import UserMessage
        # 必须此处import operation model 否则和operation中的import user的model 形成循环调用
        return UserMessage.objects.filter(user=self.id, has_read= False).count() # 此处id是int类型 而不是外键


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

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name