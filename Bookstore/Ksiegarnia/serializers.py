from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Price', 'Publisher','owner']

class CustomerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Customer
        fields = ['First_Name', 'Last_Name', 'Birth_Date', 'Adress', 'Phone_Number', 'Email', 'owner']


class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Employee
        fields = ['Name', 'Last_Name', 'Position', 'owner']

class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Transaction
        fields = ['Price', 'Employee', 'Book', 'Customer', 'owner']


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  #  questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']

"""""
class BookSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length=45)
    Author = serializers.CharField(max_length=45)
    Price = serializers.DecimalField(decimal_places=2, max_digits=5)
    Publisher = serializers.CharField(max_length=45)

    def create(self, validated_data):
        return Book.objects.create(*validated_data)

class CustomerSerializer(serializers.Serializer):
    First_Name = serializers.CharField(max_length=45)
    Last_Name = serializers.CharField(max_length=45)
    Birth_Date = serializers.DateField()
    Adress = serializers.CharField(max_length=90)
    Phone_Number = serializers.CharField(max_length=12)
    Email = serializers.CharField(max_length=45)

class EmployeeSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=45)
    Last_Name = serializers.CharField(max_length=45)
    Position = serializers.CharField(max_length=45)


class TransactionSerializer(serializers.Serializer):
    Price = serializers.DecimalField(decimal_places=2, max_digits=5)
    date = serializers.DateField()
    Employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    Book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    Customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
"""""