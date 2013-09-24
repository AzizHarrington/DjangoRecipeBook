from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Dish(models.Model):
    new = models.BooleanField()
    name = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
    flavors = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    prep_time = models.FloatField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
