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

import authapp.views as authapp
from django.urls import path, re_path
app_name = 'authapp'

urlpatterns = [
    re_path('^login/$', authapp.userlogin, name='login'),
    re_path('^logout/$', authapp.userlogout, name='logout'),
    re_path('^register/$', authapp.user_register, name='register'),
    re_path('^update/$', authapp.user_update, name='update'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]
