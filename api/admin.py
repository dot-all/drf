from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario

    list_display = ('email', 'rut_user', 'dv_user', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'rut_user')
    ordering = ('email',)

    readonly_fields = ('fecha_modificacion',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'rut_user', 'dv_user')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login',)}),  # 👈 quitamos 'date_joined'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'rut_user', 'dv_user', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Usuario, UsuarioAdmin)
