from celery import task

from .models import Blog


@task()
def crawl(blog_id, limit=10):
    blog = Blog.objects.get(id=blog_id)
