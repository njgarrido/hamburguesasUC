from rest_framework import serializers

from api.models import Ingredient, Burguer

class BurguerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Burguer
        fields = ('id_burguer', 'name', 'description', 'price', 'image', 'ingredients')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id_ingredient', 'name', 'description')