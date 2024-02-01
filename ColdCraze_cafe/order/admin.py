from django.contrib import admin
from order.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
   list_display = ['id','snacks','snack_quantity','drink_quantity','deserts','desert_quantity']
   
admin.site.register(Order,OrderAdmin)
