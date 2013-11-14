import os
from datetime import datetime
from time import strftime

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from boto.s3.key import Key
from boto import connect_s3

import Recipes.settings.base as settings
from .models import Dish, Ingredient
from .forms import DishForm



def home(request):
    return render(request, 'front.html')


def list_view(request):
    dishes = Dish.objects.all()
    return render(request, 'list.html', {'dishes': dishes})


def detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'detail.html', {'dish': dish})


def new(request):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse('list'))
    else:
        form = DishForm()
    return render(request, 'new.html', {'form': form})



def edit(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect(reverse('detail', args=(pk, )))
    else:
        form = DishForm(instance=dish)
    return render(request, "edit.html", {"form": form, "dish": dish})




def delete(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == "POST":
        dish.ingredients.all().delete()
        dish.delete()
        return redirect(reverse('list'))
    return render(request, "delete.html", {"dish": dish})


