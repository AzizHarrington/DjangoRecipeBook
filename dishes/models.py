from time import time

from django.db import models
from django.contrib.auth.models import User 


def get_upload_file_name(instance, filename):
    return "uploaded/%s_%s" % (str(time()).replace('.', '_'), filename)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Dish(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, null=True)
    photo = models.FileField(upload_to=get_upload_file_name, null=True, blank=True)
    cuisine = models.CharField(max_length=200)
    flavors = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    prep_time = models.IntegerField()
    comments = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-likes',)
