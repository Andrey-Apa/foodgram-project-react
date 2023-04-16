from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.forms import ModelForm

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


class SuscriptionsForm(ModelForm):
    class Meta:
        model = Subscriptions
        fields = ('user', 'author',)

    def clean(self):
        cleaned_data = super(SuscriptionsForm, self).clean()
        if cleaned_data.get('user') == cleaned_data.get('author'):
            raise ValidationError('Нельзя подписаться на самого себя!')
        return cleaned_data


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    form = SuscriptionsForm
    list_display = ('user', 'author',)
    search_fields = ('user', 'author',)
