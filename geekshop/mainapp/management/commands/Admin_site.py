from django.core.management.base import BaseCommand
from mainapp.models import ProductCategoru, Product
#from django.contrib.auth.models import User
from authapp.models import ShopUser
import os
import json

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategoru.objects.all().delete()
        for category in categories:
            new_category = ProductCategoru(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategoru.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            Product(**product).save()

        # Создаем суперпользователя при помощи менеджера модели
        user = ShopUser.objects.filter(username='django')
        if not user:
            print('создан новый суперпользователь')
            ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=23)