from django.contrib import admin
from .models import (
    Tour, PickupLocations, Category,
    Program, Equipment, Included,
    NotIncluded, Duration, TourDates,
    TourImage
)
from apps.common.admin.mixin import BaseAdmin


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]
    list_display = ('title', 'category', 'start_date', 'end_date', 'archived')
    list_filter = ('category', 'difficulty', 'archived')
    # fields = ('category', 'title', 'point', 'duration', 'price', 'description', 'difficulty', 'views', 'tags',
    #           'pickup_locations', 'program', 'equipment', 'included', 'not_included', 'start_date',
    #           'end_date', 'tour_dates', 'archived','is_favorite')


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(BaseAdmin):
    list_display = ('id', 'title', 'time')
    search_fields = ('title', 'time',)


@admin.register(Equipment)
class EquipmentAdmin(BaseAdmin):
    pass


@admin.register(PickupLocations)
class PickupLocationsAdmin(BaseAdmin):
    pass


@admin.register(Included)
class IncludedAdmin(BaseAdmin):
    pass


@admin.register(NotIncluded)
class NotIncludedAdmin(BaseAdmin):
    pass


@admin.register(Duration)
class NotIncludedAdmin(BaseAdmin):
    pass


@admin.register(TourDates)
class TourDatesAdmin(BaseAdmin):
    list_display = ('id', 'date',)
    search_fields = 'date',

