from django.urls import path
from menu.views import menu
from menu.views import item_detail
from menu.views import filter_by_category
from menu.views import filter_by_price_range
# menu/urls.py

urlpatterns = [
    path('', menu, name='menu'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('filter/category/<str:category>/', filter_by_category, name='filter_by_category'),
    path('filter/price/<int:min_price>/<int:max_price>/', filter_by_price_range, name='filter_by_price_range'),
]


