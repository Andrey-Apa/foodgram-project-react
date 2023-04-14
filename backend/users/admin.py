from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Subscriptions


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'is_active', 'username', 'first_name', 'last_name', 'email',
    )
    fields = (
        ('username', 'email', ),
        ('first_name', 'last_name', ),
        ('is_active', 'password', ),
    )
    fieldsets = []
    search_fields = ('username', 'email',)
    list_filter = ('is_active', 'first_name', 'email',)
    save_on_top = True


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
    search_fields = ('user', 'author',)
    save_on_top = True
