from django.contrib import admin
from .models import Tour, PickupLocations, Category


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    ...


@admin.register(PickupLocations)
class PickupLocationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)
