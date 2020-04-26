from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BurguerSerializer, IngredientSerializer
from .models import Burguer, Ingredient


class BurguerViewSet(viewsets.ModelViewSet):
    queryset = Burguer.objects.all().order_by('name')
    serializer_class = BurguerSerializer

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, id=None):
        burguer = Burguer.objects.get(id_burguer=id)

    def destroy(self, request, pk=None):
        burguer = Burguer.objects.get(id_burguer=pk)
        burguer.delete()


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer

    def update(self, request, id=None):
        pass

    def partial_update(self, request, id=None):
        ingredient = Ingredient.objects.get(id_ingredient=id)

    def destroy(self, request, pk=None):
        ingredient = Ingredient.objects.get(id_ingredient=pk)
        burguers = ingredient.burguer_set.all()
        if not burguers:
            ingredient.delete()
