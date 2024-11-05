from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'is_superuser', 'is_active']
    search_fields = ['phone_number', 'email', 'firstname']
    # fields = ('phone_number', 'firstname', 'lastname', 'email', 'birth_date', 'avatar',
    #           'is_superuser', 'groups', 'is_staff', 'date_joined', 'user_permissions',
    #           'is_active', 'is_blocked', 'code')

    def display_name(self, obj):
        return f'{obj.first_name}:{obj.last_name} - {obj.phone_number}'

    display_name.short_description = 'Firstname'
