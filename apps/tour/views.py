from django.contrib.auth.models import AnonymousUser
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from .filters import TourFilter
from .models import Tour, Category
from .serializers import TourSerializer, TourCardSerializer, CategorySerializer


@extend_schema(tags=['Category'])
class CategoryView(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['Tour'])
class TourApiView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Tour.objects.all()
    serializer_class = TourCardSerializer
    filterset_class = TourFilter

    def get_queryset(self):
        user = self.request.user
        queryset = Tour.objects.all()

        if isinstance(user, AnonymousUser):
            return queryset

        favorite_tour = Tour.objects.filter(

        )
