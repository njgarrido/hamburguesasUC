from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BurguerSerializer, IngredientSerializer
from .models import Burguer, Ingredient


class BurguerViewSet(viewsets.ModelViewSet):
    queryset = Burguer.objects.all().order_by('name')
    serializer_class = BurguerSerializer
    # lookup_url_kwarg = "asd"

    def create(self, request):
        serializer = BurguerSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"code": "201", "descripcion": 'operacion exitosa'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"code": "400", "descripcion": 'operacion fallida'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        if request.method == "GET":
            return Response(
                {"code": "200", "descripcion": 'resultados obtenidos'},
                status=status.HTTP_200_OK
            )
        elif request.method == "POST":
            return Response(
                {"code": "201", "descripcion": 'ingrediente cread0'},
                status=status.HTTP_201_CREATED
            )

    def partial_update(self, request, pk=None):
        try:
            aux = int(pk)
        except:
            return Response(
                {"code": "400", "descripcion": 'id invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            burguer = Burguer.objects.get(id_burguer=pk)
        except:
            return Response(
                {"code": "404", "descripcion": 'hamburguesa inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )

        if "id_burguer" in request.data or "ingredients" in request.data:
            return Response(
                {"code": "400", "descripcion": 'parametros invalidos'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BurguerSerializer(
            burguer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"code": "200", "descripcion": 'operacion exitosa'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"code": "400", "descripcion": 'parametros invalidos'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        try:
            burguer = Burguer.objects.get(id_burguer=pk)
        except:
            return Response(
                {"code": "201", "descripcion": 'hamburguesa creada'},
                status=status.HTTP_201_CREATED
            )
        burguer.delete()
        return Response(
            {"code": "404", "descripcion": 'hamburguesa inexistente'},
            status=status.HTTP_404_NOT_FOUND
        )

    @action(detail=True, methods=['put', 'delete'], url_path='ingrediente/(?P<pk2>[^/.]+)')
    def ingrediente(self, request, pk=None, pk2=None):
        try:
            burguer = Burguer.objects.get(id_burguer=pk)
        except:
            return Response(
                {"code": "400", "descripcion": 'Id de hamburguesa inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if request.method == 'PUT':
            try:
                ingredient = Ingredient.objects.get(id_ingredient=pk2)
            except:
                return Response(
                    {"code": "404", "descripcion": 'ingrediente inexistente'},
                    status=status.HTTP_404_NOT_FOUND
                )
            burguer.ingredients.add(ingredient)
            return Response(
                {"code": "201", "descripcion": 'ingrediente agregado'},
                status=status.HTTP_404_NOT_FOUND
            )
        if request.method == 'DELETE':
            try:
                ingredient = Ingredient.objects.get(id_ingredient=pk2)
                burguer.ingredients.remove(ingredient)
            except:
                return Response(
                    {"code": "404", "descripcion": 'Ingrediente inexistente en la hamburguesa'},
                    status=status.HTTP_404_NOT_FOUND
                )
            # burguer.save()
            return Response(
                {"code": "200", "descripcion": 'Ingrediente retirado'},
                status=status.HTTP_200_OK
            )


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer

    def create(self, request):
        serializer = IngredientSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"code": "201", "descripcion": 'operacion exitosa'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"code": "400", "descripcion": 'operacion fallida'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, id=None):
        if request.method == "GET" or request.method == "get":
            return Response(
                {"code": "200", "descripcion": 'resultados obtenidos'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"code": "201", "descripcion": 'ingrediente cread0'},
                status=status.HTTP_201_CREATED
            )

    def partial_update(self, request, id=None):
        try:
            aux = int(id)
        except:
            return Response(
                {"code": "400", "descripcion": 'id invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            ingredient = Ingredient.objects.get(id_ingredient=id)
        except:
            return Response(
                {"code": "404", "descripcion": 'ingrediente inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"code": "200", "descripcion": 'operacion exitosa'},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        try:
            ingredient = Ingredient.objects.get(id_ingredient=pk)
        except:
            return Response(
                {"code": "404", "descripcion": 'ingrediente inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        burguers = ingredient.burguer_set.all()
        if not burguers:
            ingredient.delete()
            return Response(
                {"code": "200", "descripcion": 'ingrediente eliminado'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"code": "409", "descripcion": 'Ingrediente no se puede borrar, se encuentra presente en una hamburguesa'},
                status=status.HTTP_409_CONFLICT
            )
