# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
import random

class Migration(DataMigration):

    def forwards(self, orm):
        page_count = orm.Page.objects.count()
        for i in range(3):
            index = random.randint(1, page_count)
            page = orm.Page.objects.get(id=index)
            page.views = random.randint(1, 100)
            page.save()

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration")

    models = {
        u'rango.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'rango.page': {
            'Meta': {'object_name': 'Page'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rango.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['rango']
    symmetrical = True
