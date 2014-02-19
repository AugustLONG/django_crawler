# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table(u'crawler_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, db_index=True)),
            ('post_title_xpath', self.gf('django.db.models.fields.TextField')()),
            ('post_content_xpath', self.gf('django.db.models.fields.TextField')()),
            ('post_date_xpath', self.gf('django.db.models.fields.TextField')(null=True)),
            ('post_comments_xpath', self.gf('django.db.models.fields.TextField')(null=True)),
            ('next_page_xpath', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'crawler', ['Blog'])

        # Adding model 'Post'
        db.create_table(u'crawler_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Blog'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'crawler', ['Post'])

        # Adding model 'Comment'
        db.create_table(u'crawler_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Post'])),
            ('md5_hash', self.gf('django.db.models.fields.CharField')(max_length=32, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'crawler', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table(u'crawler_blog')

        # Deleting model 'Post'
        db.delete_table(u'crawler_post')

        # Deleting model 'Comment'
        db.delete_table(u'crawler_comment')


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
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['crawler']