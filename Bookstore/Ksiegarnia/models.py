from _json import make_encoder

from django.db import models

# Create your models here.
class Customer(models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    Birth_Date = models.DateField()
    Adress = models.CharField(max_length=90)
    Phone_Number = models.CharField(max_length=12)
    Email = models.CharField(max_length=45)

class Employee(models.Model):
    Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    Position = models.CharField(max_length=45)

class Book(models.Model):
    Title = models.CharField(max_length=45)
    Author = models.CharField(max_length=45)
    Price = models.DecimalField(decimal_places=2, max_digits=5)
    Publisher = models.CharField(max_length=45)

class Magazine(models.Model):
    Amount = models.IntegerField()
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)

class Transaction(models.Model):
    Price = models.DecimalField(decimal_places=2, max_digits=5),
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


