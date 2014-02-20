from contextlib import closing
import hashlib

from selenium import webdriver

from .models import Blog, Post, Comment
from project.celery import app


def explore_posts(blog_id, url):
    blog = Blog.objects.get(id=blog_id)

    with closing(webdriver.Firefox()) as browser:
        browser.get(url)
        for link in browser.find_elements_by_xpath(blog.post_url_xpath):
            post, created = Post.objects.get_or_create(
                blog_id=blog.pk,
                url=link.get_attribute('href'))
            crawl_post.delay(post.pk)


@app.task()
def crawl_blog(blog_id):
    blog = Blog.objects.get(id=blog_id)

    with closing(webdriver.Firefox()) as browser:
        url = blog.url
        while True:
            explore_posts(blog.pk, url)
            browser.get(url)
            next_page_sel = browser.find_element_by_xpath(blog.next_page_xpath)
            url = next_page_sel.get_attribute('href')
            if not url:
                break


@app.task()
def crawl_post(post_id):
    post = Post.objects.get(id=post_id)
    blog = post.blog

    with closing(webdriver.Firefox()) as browser:
        browser.get(post.url)

        # extract post title
        sel = browser.find_element_by_xpath(blog.post_title_xpath)
        post.title = sel.text
        # extract post content
        sel = browser.find_element_by_xpath(blog.post_content_xpath)
        post.content = sel.text
        # extract post date
        sel = browser.find_element_by_xpath(blog.post_date_xpath)
        post.date = sel.text
        post.save()

        # find and save the comments
        for sel in browser.find_elements_by_xpath(blog.post_comments_xpath):
            content = sel.text
            comment, created = Comment.objects.get_or_create(
                post_id=post.pk,
                md5_hash=hashlib.md5(content.encode('utf-8')).hexdigest())
            if created:
                comment.content = content
                comment.save()
