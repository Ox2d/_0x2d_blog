from django.conf.urls import url
from blog.views import IndexView, ArticleView, CategoryView, TagView

urlpatterns = [
        url(r'^$',IndexView.as_view()),
        url(r'^article/(?P<slug>\w+)$',ArticleView.as_view()),
        url(r'^category/(?P<category>\w+)/$',CategoryView.as_view()),
        url(r'^tag/(?P<tag>\w+)/$',TagView.as_view()),
]