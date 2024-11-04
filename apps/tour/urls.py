from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    TourApiView, CategoryView, FavoriteTourViewSet,
    UpcomingToursApiView
)

router = DefaultRouter()
router.register('tour', TourApiView, basename='api_tour')
router.register('category', CategoryView, 'api_category')
router.register('favorite', FavoriteTourViewSet, 'api_favorite')
router.register('upcoming-tour', UpcomingToursApiView, 'api_upcoming-tour')


urlpatterns = [
]


urlpatterns += router.urls