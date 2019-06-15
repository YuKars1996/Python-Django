from django.contrib import admin

# Register your models here.
from mainapp.models import ProductCategoru, Product

admin.site.register(ProductCategoru)
admin.site.register(Product)