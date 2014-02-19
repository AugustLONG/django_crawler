from django.contrib import admin

from .models import Blog, Post, Comment
from .tasks import crawl as crawl


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    actions = ['crawl_blogs']

    def crawl_blogs(self, request, queryset):
        for blog in queryset:
            crawl.delay(blog.id)
        self.message_user(request, 'Task(s) created')
    crawl_blogs.short_description = 'Crawls the selected blog(s)'


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

