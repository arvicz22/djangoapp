# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Testimonial'
        db.create_table(u'signups_testimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('signups', ['Testimonial'])


    def backwards(self, orm):
        # Deleting model 'Testimonial'
        db.delete_table(u'signups_testimonial')


    models = {
        u'signups.signup': {
            'Meta': {'object_name': 'SignUp'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'for_you': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'signups.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['signups']