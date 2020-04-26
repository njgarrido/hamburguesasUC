from rest_framework import serializers

from api.models import Ingredient, Burguer

class BurguerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burguer
        fields = ('id_burguer', 'name', 'description', 'price', 'image', 'ingredients')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id_ingredient', 'name', 'description')