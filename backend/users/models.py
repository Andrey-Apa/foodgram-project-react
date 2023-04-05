from django.contrib.auth.models import AbstractUser

from django.db import models

from .validators import validate_username


class User(AbstractUser):
    """Кастомная модель пользователя."""
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True
    )
    username = models.CharField(
        verbose_name='Уникальный юзернейм',
        max_length=150,
        unique=True,
        validators=(validate_username,)
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150,
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
        default=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = (
            models.UniqueConstraint(
                fields=('username', 'email'),
                name='unique_login_fields'
            ),
        )

    def __str__(self) -> str:
        return f'{self.username}: {self.email}'


class Subscriptions(models.Model):
    """Модель подписок."""
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='subscriber')
    author = models.ForeignKey(
        User,
        verbose_name='Автор рецепта',
        on_delete=models.CASCADE,
        related_name='subscription')

    class Meta:
        ordering = ('-user',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription',
            ),
            models.CheckConstraint(
                check=~models.Q(author=models.F('user')),
                name='%(app_label)s_%(class)s_prevent_self_subscription'
            )
        )

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
