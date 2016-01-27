# coding=utf-8

from django.template.response import TemplateResponse
from django.http import HttpResponse,Http404
from _0x2d_blog.settings import PAGE_NUM
from django.views.generic import ListView, DetailView
from blog.models import Article, Category

import logging

def index(request):
    return TemplateResponse(request, 'blog/index.html')

logger = logging.getLogger(__name__)


class BaseMixin(object):

    def get_context_data(self,*args,**kwargs):
        context = super(BaseMixin,self).get_context_data(**kwargs)
        try:
            # #热门文章
            context['hot_article_list'] = Article.objects.order_by("-create_time")[0:10]
            # #导航条
            # context['nav_list'] =  Nav.objects.filter(status=0)
            # #最新评论
            # context['latest_comment_list'] = Comment.objects.order_by("-create_time")[0:10]

        except Exception as e:
            logger.error(u'[BaseMixin]加载基本信息出错')

        return context


class IndexView(BaseMixin,ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 5 #分页--每页的数目

    def get_context_data(self,**kwargs):
        #轮播
        # kwargs['carousel_page_list'] = Carousel.objects.all()
        return super(IndexView,self).get_context_data(**kwargs)

    def get_queryset(self):
        article_list = Article.objects.order_by("-update_time")
        return article_list

class ArticleView(BaseMixin,DetailView):
    queryset = Article.objects.filter()
    template_name = 'blog/article.html'
    context_object_name = 'article'
    slug_field = 'id'

    def get(self,request,*args,**kwargs):
        #统计文章的访问访问次数
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        self.cur_user_ip = ip

        id = self.kwargs.get('slug')

        return super(ArticleView,self).get(request,*args,**kwargs)


    def get_context_data(self,**kwargs):
        #评论
        # en_title = self.kwargs.get('slug','')
        # kwargs['comment_list'] = self.queryset.get(en_title=en_title).comment_set.all()
        return super(ArticleView,self).get_context_data(**kwargs)

class TagView(BaseMixin,ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = PAGE_NUM

    def get_queryset(self):
        tag = self.kwargs.get('tag','')
        article_list = Article.objects.only('tags').filter(tags__icontains=tag);

        return article_list


class CategoryView(BaseMixin,ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = PAGE_NUM

    def get_queryset(self):
        category = self.kwargs.get('category','')
        try:
            article_list = Category.objects.get(name=category).article_set.all()
        except Category.DoesNotExist:
            logger.error(u'[CategoryView]此分类不存在:[%s]' % category)
            raise Http404

        return article_list