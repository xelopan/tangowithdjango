# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.password_salt'
        db.add_column(u'southtut2_user', 'password_salt',
                      self.gf('django.db.models.fields.CharField')(max_length=8, null=True),
                      keep_default=False)

        # Adding field 'User.password_hash'
        db.add_column(u'southtut2_user', 'password_hash',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.password_salt'
        db.delete_column(u'southtut2_user', 'password_salt')

        # Deleting field 'User.password_hash'
        db.delete_column(u'southtut2_user', 'password_hash')


    models = {
        u'southtut2.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['southtut2']