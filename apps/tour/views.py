import pdb

from django.contrib.auth.models import AnonymousUser
from django.db.models import Exists, OuterRef, Value
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from .filters import TourFilter
from .models import Tour, Category, FavoriteTour
from .serializers import TourCardSerializer, CategorySerializer


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

        if isinstance(user, AnonymousUser):
            queryset = Tour.objects.annotate(is_favorite=Value(False))
        else:
            favorite_tours = FavoriteTour.objects.filter(user=user)
            queryset = Tour.objects.annotate(
                is_favorite=Exists(favorite_tours.filter(tour_id=OuterRef('id')))
            )
        return (queryset
                .prefetch_related('images')
                .prefetch_related('tour_dates')
                .select_related('duration')
                )
