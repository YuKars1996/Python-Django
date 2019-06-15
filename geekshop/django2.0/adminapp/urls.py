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

import adminapp.views as adminapp
from django.urls import path, re_path
app_name = 'adminapp'

urlpatterns = [
    #re_path('^users/read/$', adminapp.index, name='index'),
    re_path('^users/read/$', adminapp.UsersListView.as_view(), name='index'),
    re_path('^user/create/$', adminapp.user_create, name='user_create'),
    re_path('^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path('^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    re_path('^categories/$', adminapp.categories, name='categories'),
    #re_path('^category/create/$', adminapp.category_create, name='category_create'),
    re_path('^category/create/$', adminapp.ProductCategoruCreateView.as_view(), name='category_create'),
    #re_path('^category/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    re_path('^category/update/(?P<pk>\d+)/$', adminapp.ProductCategoruUpdateView.as_view(), name='category_update'),
    #re_path('^category/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),
    re_path('^category/delete/(?P<pk>\d+)/$', adminapp.ProductCategoruDeleteView.as_view(), name='category_delete'),
    re_path('^products/category/(?P<pk>\d+)/$', adminapp.products, name='products'),
   # re_path('^product/read/(?P<pk>\d+)/$', adminapp.product_read, name='product_read'),
re_path('^product/read/(?P<pk>\d+)/$', adminapp.ProductDetailView.as_view(), name='product_read'),
    re_path('^product/create/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    re_path('^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path('^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),
]
