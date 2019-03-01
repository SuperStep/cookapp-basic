from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Recipie, Ingredient
from .forms import IngredentAddForm
import logging

logger = logging.getLogger(__name__)

def recipies_list(request):
    recipies = Recipie.objects.all()
    for i in recipies:
        print(i.ingredients)
    return render(request, 'cook/recipies_list.html', {'recipies': recipies})

def recipie_detail(request, pk):
    recipie = get_object_or_404(Recipie, pk=pk)
    if request.method.lower()  == "post":      
        ingr_pk = request.POST.get('pk')
        ingredient = get_object_or_404(Ingredient, pk=ingr_pk)         
        recipie.ingredients.add(ingredient)
        recipie.save()
    
    ingredients = Ingredient.objects.all()
    return render(request, 'cook/recipie_detail.html', {'recipie': recipie, 'ingredients': ingredients})

def recipie_detail_delete(request, pk, ingredient_pk):
    recipie = get_object_or_404(Recipie, pk=pk)
    if request.method.lower() == "post": 
        ingredient = get_object_or_404(Ingredient, pk=ingredient_pk)         
        recipie.ingredients.remove(ingredient)
        recipie.save()    

    return redirect('recipie_detail', pk)