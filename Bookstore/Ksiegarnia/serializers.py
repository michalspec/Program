from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['title', 'author', 'publisher', 'price']
