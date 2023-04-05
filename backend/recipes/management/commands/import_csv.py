from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    Ingredient.objects.all().delete()

    def handle(self, **options):
        with open('../data//ingredients.csv', encoding='utf-8') as file:
            for line in file:
                ing = line.split(',')
                Ingredient.objects.get_or_create(
                    name=ing[0],
                    measurement_unit=ing[1]
                )
