from django import forms
from .models import Dish


class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'photo', 'cuisine', 'flavors', 
                  'prep_time', 'ingredients', 'comments')

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self._user = kwargs.pop('user')
        super(DishForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(DishForm, self).save(commit=False)
        inst.author = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst