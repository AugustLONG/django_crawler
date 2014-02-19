from django.contrib import admin

from .models import Blog, Post, Comment
from .tasks import crawl_blog, crawl_post


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    actions = ['crawl']

    def crawl(self, request, queryset):
        for blog in queryset:
            crawl_blog.delay(blog.id)
        self.message_user(request, 'Task(s) created')
    crawl.short_description = 'Crawls the selected blog(s)'


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'url']
    actions = ['crawl']

    def crawl(self, request, queryset):
        for post in queryset:
            crawl_post.delay(post.id)
        self.message_user(request, 'Task(s) created')
    crawl.short_description = 'Crawls the selected post(s)'


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

