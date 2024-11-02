from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TourApiView, CategoryView

router = DefaultRouter()
router.register('tour', TourApiView, basename='api_tour')
router.register('category', CategoryView, 'api_category')



urlpatterns = [
]


urlpatterns += router.urls