from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Book)
admin.site.register(Employee)
admin.site.register(Transaction)
admin.site.register(Customer)
admin.site.register(Magazine)
