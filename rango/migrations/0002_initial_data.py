# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        python_cat = orm.Category(name="Python")
        python_cat.save()

        p = orm.Page(category=python_cat,
            title="Official Python Tutorial",
            url="http://docs.python.org/2/tutorial")
        p.save()

        p = orm.Page(category=python_cat,
            title="How to Think Like a Computer Scientist",
            url="http://www.greenteapress/thinkpython")
        p.save()

        p = orm.Page(category=python_cat,
            title="Learn Python in 10 Minutes",
            url="http://korokithakis.net/tutorials/python")
        p.save()

        django_cat = orm.Category(name="Django")
        django_cat.save()

        p = orm.Page(category=django_cat,
            title="Official Django Tutorial",
            url="https://docs.djangoproject.com/en/1.5/intro/tutorial01")
        p.save()

        p = orm.Page(category=django_cat,
            title="Django Rocks",
            url="http://www.djangorocks.com")
        p.save()

        p = orm.Page(category=django_cat,
            title="How to Tango with Django",
            url="http://www.tangowithdjango.com")
        p.save()

        frame_cat = orm.Category(name="Other Frameworks")
        frame_cat.save()

        p = orm.Page(category=frame_cat,
            title="Bottle",
            url="http://bottlepy.org/docs/dev")
        p.save()

        p = orm.Page(category=frame_cat,
            title="Flask",
            url="http://flask.pocoo.org")
        p.save()
        # python_cat = orm.Category.objects.create(name="Python")
        #
        # orm.Page.objects.create(category=python_cat, \
        #     title="Official Python Tutorial", \
        #     url="http://docs.python.org/2/tutorial")
        #
        # orm.Page.objects.create(category=python_cat, \
        #     title="How to Think like a Computer Scientist", \
        #     url="http://www.greenteapress.com/thinkpython")
        #
        # orm.Page.objects.create(category=python_cat, \
        #     title="Learn Python in 10 Minutes", \
        #     url="http://www.korokithakis.net/tutorials/python")
        #
        # django_cat = orm.Category.objects.create(name="Django")
        #
        # orm.Page.objects.create(category=django_cat, \
        #     title="Official Django Tutorial", \
        #     url="https://docs/djangoproject.com/en/1.5/intro/tutorial01")
        #
        # orm.Page.objects.create(category=django_cat, \
        #     title="Django Rocks", \
        #     url="http://www.djangorocks.com")
        #
        # orm.Page.objects.create(category=django_cat, \
        #     title="How to Tango with Django", \
        #     url="http://www.tangowithdjango.com")
        #
        # frame_cat = orm.Category.objects.create("Other Frameworks")
        #
        # orm.Page.objects.create(category=frame_cat, \
        #     title="Bottle", \
        #     url="http://bottlepy.org/docs/dev")
        #
        # orm.Page.objects.create(category=frame_cat, \
        #     title="Flask", \
        #     url="http://flask.pocoo.org")

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

    models = {
        u'rango.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
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
