from django.contrib import admin
from menu.models import MenuItem
# Register your models here.
# CraveBites/menu/admin.py

# CraveBites/menu/admin.py

class PriceFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return [
            ('0-200', '0 to 200 Rs'),
            ('200-300', '200 to 300 Rs'),
            ('300-500', '300 to 500 Rs'),
            ('500-', 'Above 500 Rs'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '0-200':
            return queryset.filter(price__range=(0, 200))
        elif self.value() == '200-300':
            return queryset.filter(price__range=(200, 300))
        elif self.value() == '300-500':
            return queryset.filter(price__range=(300, 500))
        elif self.value() == '500-':
            return queryset.filter(price__gte=500)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    search_fields = ['name', 'category', 'description']
    list_filter = ['category', PriceFilter]

