from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategoru, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

def get_basket(user):
    if user.is_authenticated:
        return user.basket_set.all().order_by('product__category')
    return []

def main(request, category_pk=None):
    products = Product.objects.filter(category=2, is_active=True)
    products2 = Product.objects.filter(category=4, is_active=True)
    context = {
        'title': 'главная',
        'products': products,
        'products2': products2,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context)


def colls(request):
    context = {
        'title': 'контакты',
        'colls': colls,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/colls.html', context)


def catalog(request, pk=None, page=1):
    categories = ProductCategoru.objects.filter(is_active=True)
    if pk:
        if pk == "0":
            products = Product.objects.filter(is_active=True)
            products_paginator = Paginator(products, 8)
            try:
                products = products_paginator.get_page(page)
            except PageNotAnInteger:
                products = products_paginator.get_page(1)
            except EmptyPage:
                products = products_paginator.get_page(products_paginator.num_pages)
        else:
            products = Product.objects.filter(category__pk=pk, is_active=True)
            products_paginator = Paginator(products, 3)
            try:
                products = products_paginator.get_page(page)
            except PageNotAnInteger:
                products = products_paginator.get_page(1)
            except EmptyPage:
                products = products_paginator.get_page(products_paginator.num_pages)
        context = {
            'title': 'каталог',
            'products': products,
            'categories': categories,
            'basket': get_basket(request.user),
            'category_pk': pk,

        }
        return render(request, 'mainapp/product_list.html', context)
    else:
        #products = Product.objects.all()
        #products = Product.objects.filter(category=5)
        categories = ProductCategoru.objects.filter(is_active=True)
        products = Product.objects.filter(is_active=True)
        hot_product = random.choice(products)
        same_products = Product.objects.filter(category=hot_product.category, is_active=True). \
            exclude(pk=hot_product.pk)
        context = {
            'title': 'каталог',
            'categories': categories,
            'products': products,
            'basket': get_basket(request.user),
            'hot_product': hot_product,
            'same_products': same_products,

        }
        return render(request, 'mainapp/catalog.html', context)

def product(request, pk):
    categories = ProductCategoru.objects.filter(is_active=True)
    context = {
        'title': 'продукты',
        'categories': categories,
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', context)


def training(request):
    context = {
        'page_title': 'доставка',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/training.html', context)


