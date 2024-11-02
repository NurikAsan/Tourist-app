from django_filters import (
    RangeFilter, MultipleChoiceFilter,
    ModelMultipleChoiceFilter, FilterSet,
    ModelChoiceFilter, ChoiceFilter, CharFilter
)
from apps.tour.models import Tour, Duration, Category, FavoriteTour


class BaseFilter(FilterSet):
    order_by_price = ChoiceFilter(
        method='filter_by_price',
        label='Сортировка по цене',
        choices=(
            ('desc', 'Сначала дорогие'),
            ('asc', 'Сначала дешевые'),
        ),
    )

    def filter_by_price(self, queryset, name, value):
        price_field = self.price_field
        if value == 'desc':
            return queryset.order_by(f'-{price_field}')
        elif value == 'asc':
            return queryset.order_by(price_field)
        return queryset


class TourFilter(BaseFilter):
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
    price_field = 'price'

    class Meta:
        model = Tour
        fields = [
            'title', 'price', 'difficulty',
            'duration', 'category', 'order_by_price'
        ]


class FavoriteTourFilter(BaseFilter):
    price = RangeFilter(field_name='tour__price')
    difficulty = MultipleChoiceFilter(
        field_name='tour__difficulty',
        choices=Tour.DIFFICULT
    )
    duration = ModelMultipleChoiceFilter(
        field_name='tour__duration',
        queryset=Duration.objects.all()
    )
    # tags = ModelMultipleChoiceFilter(field_name='tour__tags', queryset=Tags.objects.all())
    category = ModelChoiceFilter(
        field_name='tour__category',
        queryset=Category.objects.all()
    )
    title = CharFilter(
        field_name='tour__title',
        lookup_expr='startswith',
        label='Название (начинается с)'
    )
    price_field = 'tour__price'

    class Meta:
        model = FavoriteTour
        fields = ['order_by_price', 'price', 'difficulty', 'duration', 'category']
