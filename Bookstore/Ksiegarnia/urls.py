from django.urls import path
from . import views
from .views import home
from django.conf.urls import url

urlpatterns = [
    url(r'^$',home,name='home'),
    path('book/', views.BookList.as_view(),name='book'),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('employee/', views.EmployeeList.as_view(), name='employee'),
    path('employeeDetail/<int:pk>/', views.EmployeeDetail.as_view()),
    path('customer/' ,views.CustomerList.as_view(),name='customer'),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('transaction/', views.TransactionList.as_view(),name='transaction'),
    path('transaction/<int:pk>/', views.TransactionDetail.as_view()),
    path('magazine/', views.MagazineList.as_view(),name='magazine'),
    path('magazine/<int:pk>/', views.MagazineDetail.as_view()),
    path('user/', views.UserList.as_view(),name='user'),
    path('user/<int:pk>/', views.UserDetail.as_view())
    ]