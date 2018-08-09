"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from users.views import IndexView, RegisterView
import xadmin
from bbs.settings import MEDIA_ROOT
from django.views.static import serve
from topics.views import EditorView, PostView, uploadfiles_view
from users.views import LogoutView
from users.views import ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url('admin/', admin.site.urls),
    url('^$', IndexView.as_view(), name='index'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url('^captcha/', include('captcha.urls')),
    url('^topics/', include('topics.urls', namespace='topics'), ),
    url('^ed/', EditorView.as_view(), name='editor'),
    url('uploadfiles/', uploadfiles_view.as_view()),
    url('^logout/$', LogoutView.as_view(), name='logout'),  # 这里是方法，有括号
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url('^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
]
