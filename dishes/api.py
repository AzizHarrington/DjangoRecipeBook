from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Dish


class RecipeResource(ModelResource):
    class Meta:
        queryset = Dish.objects.all()
        resource_name = 'recipe'
        filtering = {'cuisine': ALL, 'id': ALL, 'name': ALL}