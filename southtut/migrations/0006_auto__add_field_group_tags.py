# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Group.tags'
        db.add_column(u'southtut_group', 'tags',
                      self.gf('southtut.fields.TagField')(default=[]),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Group.tags'
        db.delete_column(u'southtut_group', 'tags')


    models = {
        u'southtut.group': {
            'Meta': {'object_name': 'Group'},
            'facebook_page_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '144'}),
            'tags': ('southtut.fields.TagField', [], {'default': '[]'})
        },
        u'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shrubberies': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['southtut']