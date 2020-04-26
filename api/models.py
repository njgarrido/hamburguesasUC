from django.db import models

class Ingredient(models.Model):
    id_ingredient = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()


class Burguer(models.Model):
    id_burguer = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    ingredients = models.ManyToManyField(Ingredient)

