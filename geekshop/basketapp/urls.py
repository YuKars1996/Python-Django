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

import basketapp.views as basketapp
from django.urls import path, re_path
app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.index, name='main'),
    re_path('^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
    re_path('^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),
    re_path('^edit/(?P<product_pk>\d+)/(?P<quantity>\d+)/ajax/$', basketapp.basket_edit),
]
