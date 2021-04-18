from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name')}),
        ('Permissions', {'fields':('is_staff', 'is_active', 'account_type')}),
        ('Personal', {'fields': ('address',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'account_type')
        }),
    )
    list_filter = ('user_name', 'is_active', 'account_type')
    ordering = ('-created_at', 'account_type')
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'account_type')

admin.site.register(User, UserAdminConfig)