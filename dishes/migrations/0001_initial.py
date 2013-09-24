# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'dishes_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'dishes', ['Ingredient'])

        # Adding model 'Dish'
        db.create_table(u'dishes_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('new', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cuisine', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('flavors', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('prep_time', self.gf('django.db.models.fields.FloatField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'dishes', ['Dish'])

        # Adding M2M table for field ingredients on 'Dish'
        m2m_table_name = db.shorten_name(u'dishes_dish_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dish', models.ForeignKey(orm[u'dishes.dish'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'dishes.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dish_id', 'ingredient_id'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table(u'dishes_ingredient')

        # Deleting model 'Dish'
        db.delete_table(u'dishes_dish')

        # Removing M2M table for field ingredients on 'Dish'
        db.delete_table(db.shorten_name(u'dishes_dish_ingredients'))


    models = {
        u'dishes.dish': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Dish'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'flavors': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dishes.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prep_time': ('django.db.models.fields.FloatField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'dishes.ingredient': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['dishes']