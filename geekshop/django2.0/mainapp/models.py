from django.db import models

# Create your models here.
class ProductCategoru(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'ProductCategoru: {self.name} ({self.pk})'


class Product(models.Model):
    category = models.ForeignKey(ProductCategoru, verbose_name='категория продукта', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', null=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=64, blank=True)
    description = models.TextField(verbose_name='подробное описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def __str__(self):
        return f'Product: {self.name} ({self.pk})'

