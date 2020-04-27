from django.urls import include, path
from . import views
from rest_framework.routers import SimpleRouter


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()

router = OptionalSlashRouter()
router.register(r'hamburguesa', views.BurguerViewSet)
router.register(r'ingrediente', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]