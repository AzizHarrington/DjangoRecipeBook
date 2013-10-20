# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ingredient.name'
        db.alter_column(u'dishes_ingredient', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Deleting field 'Dish.new'
        db.delete_column(u'dishes_dish', 'new')

        # Adding field 'Dish.photo'
        db.add_column(u'dishes_dish', 'photo',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Dish.likes'
        db.add_column(u'dishes_dish', 'likes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Dish.flavors'
        db.alter_column(u'dishes_dish', 'flavors', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Dish.cuisine'
        db.alter_column(u'dishes_dish', 'cuisine', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Dish.name'
        db.alter_column(u'dishes_dish', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Dish.prep_time'
        db.alter_column(u'dishes_dish', 'prep_time', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'Ingredient.name'
        db.alter_column(u'dishes_ingredient', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))
        # Adding field 'Dish.new'
        db.add_column(u'dishes_dish', 'new',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Dish.photo'
        db.delete_column(u'dishes_dish', 'photo')

        # Deleting field 'Dish.likes'
        db.delete_column(u'dishes_dish', 'likes')


        # Changing field 'Dish.flavors'
        db.alter_column(u'dishes_dish', 'flavors', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Dish.cuisine'
        db.alter_column(u'dishes_dish', 'cuisine', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Dish.name'
        db.alter_column(u'dishes_dish', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Dish.prep_time'
        db.alter_column(u'dishes_dish', 'prep_time', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'dishes.dish': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Dish'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'flavors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dishes.Ingredient']", 'symmetrical': 'False'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'prep_time': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'dishes.ingredient': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dishes']