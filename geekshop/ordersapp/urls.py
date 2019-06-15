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

import ordersapp.views as ordersapp
from django.urls import path, re_path
app_name = 'ordersapp'

urlpatterns = [
    re_path('^list/$', ordersapp.OrderList.as_view(), name='index'),
    re_path('^create/$', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    re_path('^read/(?P<pk>\d+)/$', ordersapp.OrderRead.as_view(), name='order_read'),
    re_path('^update/(?P<pk>\d+)/$', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    re_path('^delete/(?P<pk>\d+)/$', ordersapp.OrderDelete.as_view(), name='order_delete'),
    re_path('^order/proceed/(?P<pk>\d+)/$', ordersapp.order_forming_complete, name='order_forming_complete'),
    re_path('^product/(?P<pk>\d+)/price/$', ordersapp.get_product_price),
]
