from django_filters import (
    RangeFilter, MultipleChoiceFilter,
    ModelMultipleChoiceFilter, FilterSet,
    ModelChoiceFilter, ChoiceFilter, CharFilter
)
from apps.tour.models import Tour, Duration, Category


class TourFilter(FilterSet):
    order_by_price = ChoiceFilter(
        method='filter_by_price',
        label='Сортировка по цене',
        choices=(
            ('desc', 'Сначала дорогие'),
            ('asc', 'Сначала дешевые'),
        ),
    )

    price = RangeFilter(field_name='price')
    difficulty = MultipleChoiceFilter(
        field_name='difficulty',
        choices=Tour.DIFFICULT
    )
    duration = ModelMultipleChoiceFilter(
        field_name='duration',
        queryset=Duration.objects.all()
    )
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all()
    )
    title = CharFilter(
        field_name='title',
        lookup_expr='startswith',
        label='Название (начинается с)'
    )

    class Meta:
        model = Tour
        fields = [
            'title', 'price', 'difficulty',
            'duration', 'category', 'order_by_price'
        ]

    def filter_by_price(self, queryset, name, value):
        if value == 'desc':
            return queryset.order_by('-price')
        elif value == 'asc':
            return queryset.order_by('price')
        return queryset
