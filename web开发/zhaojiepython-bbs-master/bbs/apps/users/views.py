from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from .forms import RegisterForm, LoginForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from topics.models import Topics
from datetime import datetime
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin
from .forms import UploadImageForm, UserInfoForm, ForgetForm
from django.http import HttpResponse
import json
from .models import UserMessage
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class IndexView(View):
    def get(self,request):
        return render(request, 'index.html',{})


class IndexView(View):
    def get(self,request):
        topics = Topics.objects.all()
        return render(request, 'index.html',{'topics': topics})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, 'index.html', {'msg': '用户未激活'})
            else:
                return render(request, 'index.html', {'msg': '用户名或密码错误'})
        else:
            return HttpResponseRedirect(reverse("index"))

class ActiveUserView(View):
    def get(self, request, active_code): # active_code和url里名字一样
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return HttpResponseRedirect(reverse("index"))


class RegisterView(View):
    def get(self, requsest):
        register_form = RegisterForm()
        return  render(requsest, 'register.html', {'register_form': register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已经存在'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.register_time = datetime.now()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            # 写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册考研论坛"
            user_message.save()

            send_register_email(user_name, 'register')
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'register.html', {'register_form': register_form})

class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form })

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        else:
            return render(request,'forgetpwd.html', {'forget_form': forget_form })


class ResetView(View):
    def get(self, request, active_code): # active_code和url里名字一样
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'index.html')


class ModifyPwdView(View):
    '''
    修改用户密码
    '''
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '') # 在html里命名了
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg':'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'index.html')
        else:
            email = request.POST.get('email', '') # email在if中，此处还要再写一次
            return render(request, 'password_reset.html', {'email': email , 'modify_form': modify_form})

class LogoutView(View):
    # 用户登出
    def get(self, request):
        logout(request)
        # 重定向到首页
        return HttpResponseRedirect(reverse("index"))



class UserinfoView(LoginRequiredMixin, View):
    # 用户个人信息
    def get(self, request):
        current_page = "info"
        return render(request, 'usercenter-info.html', {
            'current_page': current_page
        })

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class UploadImageView(LoginRequiredMixin, View):
    # 用户修改头像
    def post(self, request):
        # request.FILES保存用户上传的文件
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            # image = image_form.cleaned_data['image']
            # request.user.image = image
            image_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(View):
    '''
    个人中心修改用户密码
    '''
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail", "msg":"密码不一致"}', content_type='application/json')
            # '{"status":"fail", "msg":"密码不一致",}'大括号里多了一个逗号要命不成功
            user = request.user
            user.password = make_password(pwd2)
            user.save()
            return HttpResponse('{"status":"success" }', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')


class SendEmailCodeView(LoginRequiredMixin, View):
    '''
    发送邮箱验证码
    '''
    def get(self, request):
        email = request.GET.get('email', '')
        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已经存在"}', content_type='application/json')
        send_register_email(email, 'update_email')
        return HttpResponse('{"status":"success" }', content_type='application/json')




class UpdateEmailView(LoginRequiredMixin, View):
    # 修改个人邮箱
    def post(self, request):
        email = request.POST.get('email', '')
        code = request.POST.get('code', '')

        existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email') # 上面写成了type
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"email":"验证码错误"}', content_type='application/json')




class MyMessageView(LoginRequiredMixin, View):
    # 我的消息
    def get(self, request):
        current_page = 'message'
        all_message = UserMessage.objects.filter(user=request.user.id) # UserMessage里的user是个数字，用于后台存入消息的时候是填用户id，因此此处是user.id
        # 用户进入个人消息后清空未读记录
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()
        # 对个人消息进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_message, 5, request=request)
        messages = p.page(page)
        return render(request, 'usercenter-message.html', {
            "messages": messages,
            "current_page": current_page
        })