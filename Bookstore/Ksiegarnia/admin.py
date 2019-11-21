from django.contrib import admin
from .models import Employee
from .models import Book
from .models import Customer
from .models import Magazine
from .models import Transaction
# Register your models here.
admin.site.register(Employee)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Magazine)
admin.site.register(Transaction)

