from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

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
    pass


class Edit(View):
    pass


class Delete(View):
    pass
