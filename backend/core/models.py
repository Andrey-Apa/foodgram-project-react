from django.db.models import DateTimeField, Model


class CoreModel(Model):
    """Базовая модель."""
    date_added = DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        editable=False
    )

    class Meta:
        abstract = True
