import hashlib

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Blog(models.Model):
    name = models.CharField(_('Blog Name'), max_length=255, db_index=True)
    url = models.URLField(_('Blog Url'), db_index=True)
    post_url_xpath = models.TextField(_('Post Url Xpath'))
    post_title_xpath = models.TextField(_('Post Title Xpath'))
    post_content_xpath = models.TextField(_('Post Content Xpath'))
    post_date_xpath = models.TextField(_('Post Date Xpath'), null=True)
    post_comments_xpath = models.TextField(_('Post Comments Xpath'), null=True)
    next_page_xpath = models.TextField(_('Next Page Xpath'), null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    blog = models.ForeignKey(Blog)
    url = models.URLField(_('Post Url'), db_index=True)
    title = models.CharField(_('Title'), max_length=255, blank=True)
    content = models.TextField(_('Content'), blank=True)

    def __str__(self):
        return self.title or '*** Not scraped yet ***'


@python_2_unicode_compatible
class Comment(models.Model):
    post = models.ForeignKey(Post)
    md5_hash = models.CharField(_('Comment Hash'), max_length=32,
                                db_index=True)
    content = models.TextField(_('Content'))

    def __str__(self):
        return self.content[:40].replace('\n', ' ')

    def save(self, *args, **kwargs):
        self.md5_hash = hashlib.md5(self.content.encode('utf-8')).hexdigest()
        super(Comment, self).save(*args, **kwargs)
