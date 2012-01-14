# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Subscription.campo_novo_teste'
        db.add_column('subscription', 'campo_novo_teste', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=10), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Subscription.campo_novo_teste'
        db.delete_column('subscription', 'campo_novo_teste')


    models = {
        'subscription.subscription': {
            'Meta': {'ordering': "['created_at']", 'object_name': 'Subscription', 'db_table': "'subscription'"},
            'campo_novo_teste': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['subscription']
