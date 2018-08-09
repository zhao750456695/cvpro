# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from operations.models import UserFavorite
from django.http import HttpResponse

# Create your views here.


from .models import NewsTopic
class NewsTopicListView(View):
    def get(self, request):
        all_topics = NewsTopic.objects.all()
        hot_topics = NewsTopic.objects.order_by('click_nums')[:3]
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_topics = all_topics.filter(Q(topic_name__icontains=search_keywords) | Q(desc__icontains=search_keywords) | Q(detail__icontains=search_keywords))  # 双下划线 i一般意为不区分大小写 Q或
        sort = request.GET.get('')
        if sort:
            if sort=='hot':
                all_topics = NewsTopic.objects.order_by('-click_nums')
            elif sort =='user_nums':
                all_topics = NewsTopic.objects.order_by('-user_nums')
            # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_topics, 10, request=request)  # 数字 每页显示几个 不能少 否则会报错
        all_topics = p.page(page)
        return render(request, 'news-list.html', {'all_topics': all_topics, 'hot_topics': hot_topics, 'sort':sort}, )

class NewsDetailView(View):
    def get(self, request, topic_id):
        topic = NewsTopic.objects.get(id=topic_id)
        topic.click_nums += 1
        topic.save()
        has_fav_topic = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=topic.id, fav_type=1):
                has_fav_topic = True

        tag = topic.tag
        if tag:
            relate_topics = NewsTopic.objects.filter(tag=tag)[:1]
        else:
            relate_topics = []
        return render(request, 'news-detail.html', {'topic': topic, 'relate_topics': relate_topics, 'has_fav_topic': has_fav_topic})


class AddFavView(View):
    # 用户收藏，和取消收藏
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        # 使用用户、收藏id、收藏类型进行联合查询
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 记录已存在 表示用户取消收藏
            exist_records.delete()
            if int(fav_type) == 1:
                topic = NewsTopic.objects.get(id=int(fav_id))
                topic.fav_nums -= 1
                if topic.fav_nums < 0:
                    topic.fav_nums = 0
                topic.save()


            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')

        else:
            # 记录不存在 表示用户未收藏，并进行收藏
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    topic = NewsTopic.objects.get(id=int(fav_id))
                    topic.fav_nums += 1
                    topic.save()


                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')
