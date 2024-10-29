from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    list_display_links = "id",
    search_fields = 'title',
