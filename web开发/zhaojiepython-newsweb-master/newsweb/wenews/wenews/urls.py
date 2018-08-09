"""wenews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
import xadmin
from users.views import IndexView, LogoutView, UpdateEmailView, SendEmailCodeView, LoginView, ActiveUserView,EmailVerifyRecord, ResetView, RegisterView, ForgetPwdView, ModifyPwdView
from wenews.settings import MEDIA_ROOT
urlpatterns = [

    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^news/',include('news.urls', namespace='news')),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url('^login/$', LoginView.as_view(), name='login'),  # 这里是方法，有括号
    url('^logout/$', LogoutView.as_view(), name='logout'),  # 这里是方法，有括号
    url('^register/$', RegisterView.as_view(), name='register'),
    url('^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    # ?P(p是大写的)提取一个变量作为参数 <active_code>是变量名，再后面是正则表达式
    url('^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
     url(r'^users/', include('users.urls', namespace='users')),

]
