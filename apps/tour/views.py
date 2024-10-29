from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from .filters import TourFilter
from .models import Tour
from .serializers import TourSerializer


@extend_schema(tags=['Tour'])
class TourApiView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filterset_class = TourFilter
