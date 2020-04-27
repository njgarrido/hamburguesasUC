from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BurguerSerializer, IngredientSerializer
from .models import Burguer, Ingredient


class BurguerViewSet(viewsets.ModelViewSet):
    queryset = Burguer.objects.all().order_by('name')
    serializer_class = BurguerSerializer
    # lookup_url_kwarg = "asd"

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):

        if "id_burguer" in request.data or "ingredients" in request.data:
            return Response('fail patch, tried to change id or ingredients')

        burguer = Burguer.objects.get(id_burguer=pk)
        serializer = BurguerSerializer(
            burguer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('success patch')

        return Response('fail patch')

    def destroy(self, request, pk=None):
        burguer = Burguer.objects.get(id_burguer=pk)
        burguer.delete()

    @action(detail=True, methods=['put', 'delete'], url_path='ingrediente/(?P<pk2>[^/.]+)')
    def ingrediente(self, request, pk=None, pk2=None):
        burguer = Burguer.objects.get(id_burguer=pk)
        ingredient = Ingredient.objects.get(id_ingredient=pk2)
        if request.method == 'PUT':
            burguer.ingredients.add(ingredient)
            return Response('success put')
        if request.method == 'DELETE':
            burguer.ingredients.remove(ingredient)
            # burguer.save()
            return Response('success delete')


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
