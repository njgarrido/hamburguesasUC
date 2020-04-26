from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BurguerSerializer, IngredientSerializer
from .models import Burguer, Ingredient


class BurguerViewSet(viewsets.ModelViewSet):
    queryset = Burguer.objects.all().order_by('name')
    serializer_class = BurguerSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer