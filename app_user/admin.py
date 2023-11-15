from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

class BaseUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
      }),
    )
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email',)
    list_filter = ('email',)
    ordering = ('-id',)

admin.site.register(User, BaseUserAdmin)