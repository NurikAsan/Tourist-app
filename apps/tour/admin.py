from django.contrib import admin
from .models import (
    Tour, PickupLocations, Category,
    Program, Equipment, Included,
    NotIncluded, Duration
)
from apps.common.admin.mixin import BaseAdmin


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    ...


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
class NotIncludedAdmin(admin.ModelAdmin):
    pass
