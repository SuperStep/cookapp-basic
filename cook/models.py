from django.db import models
from django.conf import settings
from .forms import IngredentAddForm

def recipie_image_path(name):
    return 'recepies/{0}'.format(name)

class Ingredient(models.Model):
    title = models.TextField()
    description = models.TextField(default='No description')
    category = models.TextField(default='No category')
    data = models.TextField(default='{}')
    # TODO More properties

    def form(self):
        return IngredentAddForm(pk=self.pk)

    def __str__(self):
        return self.title

class Recipie(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=recipie_image_path(title))
    ingredients = models.ManyToManyField(Ingredient)
    # TODO More properties

    def __str__(self):
        return self.title

    def add_ingredinet(self):
        ingredients.append(Ingredient(title='New'))

