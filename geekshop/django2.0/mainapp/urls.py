"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import mainapp.views as mainapp
from django.urls import path, re_path
app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.main,  name='main'),
    re_path(r'^product/', mainapp.catalog, name='catalog'),
    re_path(r'^colls/', mainapp.colls, name='colls'),
    re_path(r'^training/', mainapp.training, name='training'),
    re_path(r'^catalog/category/(\d+)/$', mainapp.catalog, name='category'),
    re_path('^catalog/category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.catalog, name='category'),
    re_path(r'^catalog/product/(?P<pk>\d+)/$', mainapp.product, name='product'),
]
