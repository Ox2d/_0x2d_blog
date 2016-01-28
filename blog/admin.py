# coding=utf-8
from django.contrib import admin
from blog.models import Article,Category

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    list_display = ('name',)
    fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('category','create_time',)
    list_display = ('title','category','update_time','create_time',)
    fieldsets = (
        (u'基本信息', {
            'fields': ('title','category','tags')
            }),
        (u'内容', {
            'fields': ('content',)
            }),
    )

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'js/editor/kindeditor-4.1.10/kindeditor-all.js',
            'js/editor/kindeditor-4.1.10/lang/zh_CN.js',
            'js/editor/kindeditor-4.1.10/config.js',
            'syntax/shCore.js',
            'syntax/shAutoloader.js',
            'syntax/shBrushJava.js',
        )
        css = {'all': (
            'syntax/shCore.css',
            'syntax/shThemeDefault.css',
            'syntax/shCoreDefault.css'
        )}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)

# admin.site.register(Category)
# admin.site.register(Article)