"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from Ksiegarnia.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls')),

    path('CustomerList/', CustomerList.as_view()),
    path('CustomerDetail/<int:pk>',CustomerDetail.as_view()),

    path('EmployeeList/', EmployeeList.as_view()),
    path('EmployeeDetail/<int:pk>', EmployeeDetail.as_view()),

    path('BookList/', BookList.as_view()),
    path('BookDetail/<int:pk>', BookDetail.as_view()),

    path('MagazineList/', MagazineList.as_view()),
    path('MagazineDetail/<int:pk>', MagazineDetail.as_view()),

    path('TransactionList/', TransactionList.as_view()),
    path('TransactionDetail/<int:pk>', TransactionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)