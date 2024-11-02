from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TourApiView, CategoryView, FavoriteTourViewSet

router = DefaultRouter()
router.register('tour', TourApiView, basename='api_tour')
router.register('category', CategoryView, 'api_category')
router.register('favorite', FavoriteTourViewSet, 'api_favorite')


urlpatterns = [
]


urlpatterns += router.urls