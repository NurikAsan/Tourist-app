import pdb
from http import HTTPStatus
from django.contrib.auth.models import AnonymousUser
from django.db.models import Exists, OuterRef, Value
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import TourFilter, FavoriteTourFilter
from .models import Tour, Category, FavoriteTour
from .serializers import (
    TourCardSerializer, CategorySerializer, FavoriteTourSerializer,
    HistoryTourSerializer, PushSerializer
)


@extend_schema(tags=['Category'])
class CategoryView(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['Tour'])
class TourApiView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin):
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

    def update(self, request, *args, **kwargs):
        if isinstance(request.user, AnonymousUser):
            return Response({'message': 'Not authorize'}, status=HTTPStatus.UNAUTHORIZED)

        tour_id = int(kwargs.get('pk'))
        tour = get_object_or_404(Tour, id=tour_id)
        data = FavoriteTour.objects.filter(user=request.user, tour=tour)

        if data.exists():
            data.delete()
        else:
            FavoriteTour.objects.create(user=request.user, tour_id=tour_id)

        return Response({'message': 'success'}, status=HTTPStatus.ACCEPTED)


@extend_schema(tags=['Favorite Tour'])
class FavoriteTourViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin):
    serializer_class = FavoriteTourSerializer
    filterset_class = FavoriteTourFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            FavoriteTour
            .objects
            .filter(user=self.request.user)
            .annotate(
                is_favorite=Exists(FavoriteTour.objects.filter(tour_id=OuterRef('tour__id')))
            )
            .prefetch_related('tour__images')
            .prefetch_related('tour__tour_dates')
            .select_related('tour__duration')
        )


@extend_schema(tags=['Upcoming Tours'])
class UpcomingToursApiView(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin):
    serializer_class = HistoryTourSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pass
