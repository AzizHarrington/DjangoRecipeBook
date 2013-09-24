from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Dish, Ingredient

#Home, List, Detail, New, Edit, Delete

class Home(View):
    def get(self, request):
        return render(request, 'front.html')


class List(View):
    def get(self, request):
        dishes = Dish.objects.all()
        return render(request, 'list.html', {'dishes': dishes})


class Detail(View):
    def get(self, request, pk):
        dish = Dish.objects.get(pk=pk)
        return render(request, 'detail.html', {'dish': dish})


class New(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'new.html')
    def post(self, request, *args, **kwargs):
        dish = Dish(name=request.POST.get('name'),
                    cuisine=request.POST.get('cuisine'),
                    flavors=request.POST.get('flavors'),
                    prep_time=request.POST.get('prep_time'),
                    comments=request.POST.get('comments'))
        dish.save()
        ingredient = Ingredient(name=request.POST.get('ingredients'))
        ingredient.save()
        dish.ingredients.add(ingredient)

        return redirect('/list/')


class Edit(View):
    pass


class Delete(View):
    pass
