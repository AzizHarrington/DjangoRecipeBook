from django.contrib import admin

from .models import Dish, Ingredient


class DishAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dish, DishAdmin)  

  

class IngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingredient, IngredientAdmin)