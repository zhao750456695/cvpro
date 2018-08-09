from django.shortcuts import render
from django.views.generic.base import View
from .models import Topics, Ask, AskAnswers, AnswersReply, Attachment
from users.models import UserProfile
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json
from django.utils import timezone
# Create your views here.
class AskListView(View):
    def get(self, request, topic_id):
        topic = Topics.objects.get(id = topic_id)
        asks = Ask.objects.filter(topics=topic)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(asks, 10, request=request)  # 数字 每页显示几个 不能少 否则会报错
        asks = p.page(page)
        return render(request, 'topiclist.html', {'topic': topic, 'asks': asks})


class AskAnswersView(View):
    def get(self, request, ask_id):

        ask = Ask.objects.get(id=ask_id)
        topic = ask.topics
        answers = AskAnswers.objects.filter(ask=ask)
        return render(request, 'ask.html', {'ask': ask, 'answers': answers,'topic': topic })


class EditorView(View):
    def get(self, request):
        return render(request, 'kedit.html',{})



class PostView(View):
    """
    提问题
    """
    def get(self, request, topic_id):
        topic = Topics.objects.get(id=topic_id)
        return render(request, 'post.html', {'topic': topic})
    def post(self, request, topic_id):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        topic = Topics.objects.get(id=topic_id)
        title = request.POST.get('title')
        detail = request.POST.get('content')
        ask = Ask()
        ask.topics = topic
        ask.user = request.user
        ask.title = title
        ask.detail = detail
        ask.add_time = timezone.now()
        ask.save()
        return HttpResponseRedirect(reverse('topics:chushilist',  kwargs={"topic_id": topic.id}))

class AddAnswerView(View):
    """
    回帖
    """
    def get(self, request, ask_id):
        ask = Ask.objects.get(id=ask_id)
        return render(request, 'post.html',{'ask': ask})
    def post(self, request, ask_id):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        ask = Ask.objects.get(id=ask_id)
        title = request.POST.get('title')
        detail = request.POST.get('content')
        answer = AskAnswers()
        answer.ask = ask
        answer.add_time = timezone.now()
        answer.user = request.user
        answer.answer_title = title
        answer.answer_detail = detail
        answer.save()
        return HttpResponseRedirect(reverse('topics:chushiask',  kwargs={"ask_id": ask.id}))

class AddReplyView(View):
    """
    回复
    """
    def get(self, request, answer_id):
        answer = AskAnswers.objects.get(id=answer_id)
        return render(request, 'post.html',{'answer': answer})
    def post(self, request, answer_id):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        answer = AskAnswers.objects.get(id=answer_id)
        title = request.POST.get('title')
        detail = request.POST.get('content')
        ask = answer.ask
        reply =AnswersReply()
        reply.answer = answer
        reply.user = request.user
        reply.add_time = timezone.now()
        reply.answer_reply = detail
        reply.save()
        return HttpResponseRedirect(reverse('topics:chushiask',  kwargs={"ask_id": ask.id}))





class uploadfiles_view(View):
    """
    附件上传
    """
    def get(self, request):
        return render(request, 'editor.html')

    def post(self, request):
        dirs = request.GET.get('dir')
        print(dirs)
        file = request.FILES.get('imgFile')
        uploadfiles = Attachment()
        if dirs == 'image':
            uploadfiles.img = file
            uploadfiles.save()
            print(uploadfiles.img.url)
            dict = {
                "error": 0,
                "url": uploadfiles.img.url
            }
        elif dirs == 'file':
            uploadfiles.file = file
            uploadfiles.save()
            print(uploadfiles.file.url)
            dict = {
                "error": 0,
                "url": uploadfiles.file.url
            }
        elif dirs == 'media':
            uploadfiles.video = file
            uploadfiles.save()
            print(uploadfiles.video.url)
            dict = {
                "error": 0,
                "url": uploadfiles.video.url
            }

        return HttpResponse(json.dumps(dict))