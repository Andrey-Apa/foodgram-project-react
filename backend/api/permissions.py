from rest_framework.permissions import BasePermission, SAFE_METHODS


class BaseActivePermission(BasePermission):
    """Базовый класс разрешений с проверкой на активного пользователя.
    """
    message = 'Ваш аккаунт не активен, образитесь к администратору!'

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_active
                )


class IsAdminOrReadOnly(BaseActivePermission):
    """Права администратора или только чтение."""

    message = 'Недостаточно прав, вы не администратор!'

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.is_staff)
                )


class AuthorAdminOrReadOnly(BaseActivePermission):
    """Права активной уз автора, администратора или только чтение."""

    message = 'Недостаточно прав, аутентифицируйтесь!'

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.is_active
                    and (request.user == obj.author
                         or request.user.is_staff)
                    )
                )
