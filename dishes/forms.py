from django import forms
from .models import Dish


class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'photo', 'cuisine', 'flavors', 
                  'prep_time', 'ingredients', 'comments')

