from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import Dish, Ingredient



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
    def get(self, request):
        return render(request, 'new.html')

    def post(self, request):
        dish = Dish(name=request.POST.get('name'),
                    cuisine=request.POST.get('cuisine'),
                    flavors=request.POST.get('flavors'),
                    prep_time=request.POST.get('prep_time'),
                    comments=request.POST.get('comments'),
                )
        dish.save()

        for ingredient in request.POST.getlist('ingredient'):
            p = Ingredient(name=ingredient)
            p.save()
            dish.ingredients.add(p)

        return redirect(render('list'))


class Edit(View):
    def get(self, request, pk):
        dish = Dish.objects.get(pk=pk)
        return render(request, "edit.html", {"dish":dish})

    def post(self, request, pk):
        dish = Dish.objects.get(pk=pk)

        dish.name=request.POST.get('name')
        dish.cuisine=request.POST.get('cuisine')
        dish.flavors=request.POST.get('flavors')
        dish.prep_time=request.POST.get('prep_time')
        dish.comments=request.POST.get('comments')
        dish.save()

        dish.ingredients.all().delete()
        for ingredient in request.POST.getlist('ingredient'):
            p = Ingredient(name=ingredient)
            p.save()
            dish.ingredients.add(p)

        return redirect(reverse('detail', args=(pk,)))


class Delete(View):
    def get(self, request, pk):
        dish = Dish.objects.get(pk=pk)
        return render(request, "delete.html", {"dish": dish})

    def post(self, request, pk):
        dish = Dish.objects.get(pk=pk)
        dish.ingredients.all().delete()
        dish.delete()
        return redirect(render('list'))
