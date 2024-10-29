from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TourSearchAPIView, TourApiView

router = DefaultRouter()
router.register('tour', TourApiView, basename='api_tour')


urlpatterns = [
    path('tour/search/', TourSearchAPIView.as_view()),
]


urlpatterns += router.urls