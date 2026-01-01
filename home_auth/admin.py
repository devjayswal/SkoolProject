from django.contrib import admin
from .models import CustomUser, PasswordResetRequest
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.

class CustomUserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Roles', {'fields': ('is_student', 'is_teacher', 'is_admin')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin' 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_student', 'is_teacher', 'is_admin'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_student', 'is_teacher', 'is_admin', 'is_staff', 'is_superuser', 'is_active')

    list_filter = ('is_student', 'is_teacher', 'is_admin', 'is_staff', 'is_superuser', 'is_active')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(is_admin=False)


admin.site.register(CustomUser, CustomUserAdmin)