from django.core.management import BaseCommand
from django.db.models import Q

from mainapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product = Product.objects.filter(
            #~Q(category__name='Обувь') # ~ значит "не"
            #Q(category__name='Обувь')
            Q(category__name='Обувь') | Q(category__name='Одежда')
        )
        print(product)
