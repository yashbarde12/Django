from django.contrib import admin
from customer.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'email']

admin.site.register(Customer, CustomerAdmin)


