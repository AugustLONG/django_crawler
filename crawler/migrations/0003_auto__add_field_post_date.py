# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.date'
        db.add_column(u'crawler_post', 'date',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.date'
        db.delete_column(u'crawler_post', 'date')


    models = {
        u'crawler.blog': {
            'Meta': {'object_name': 'Blog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'next_page_xpath': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'post_comments_xpath': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'post_content_xpath': ('django.db.models.fields.TextField', [], {}),
            'post_date_xpath': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'post_title_xpath': ('django.db.models.fields.TextField', [], {}),
            'post_url_xpath': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'db_index': 'True'})
        },
        u'crawler.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5_hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crawler.Post']"})
        },
        u'crawler.post': {
            'Meta': {'object_name': 'Post'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crawler.Blog']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['crawler']