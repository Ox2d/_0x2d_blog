#coding:utf-8
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40,verbose_name=u'名称')
    # parent = models.ForeignKey('self',default=None,blank=True,null=True,verbose_name=u'上级分类')
    # rank = models.IntegerField(default=0,verbose_name=u'排序')
    # status = models.IntegerField(default=0,choices=STATUS.items(),verbose_name='状态')

    # create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        db_table = 'category'


    def __unicode__(self):
        return '%s' % (self.name)
    #     if self.parent:
    #         return '%s-->%s' % (self.parent,self.name)
    #     else:
    #         return '%s' % (self.name)

class Article(models.Model):
    category = models.ForeignKey(Category,verbose_name=u'分类')
    title = models.CharField(max_length=100,verbose_name=u'标题')
    img = models.CharField(max_length=200,default='/static/img/article.jpg')
    tags = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'标签',help_text=u'用逗号分隔')
    content = models.TextField(verbose_name=u'正文')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True)
    def get_tags(self):
        return self.tags.split(',')
    class Meta:
        db_table = 'article'
