from django.urls import path
from menu.views import menu
from menu.views import item_detail
# menu/urls.py

urlpatterns = [
    path('', menu, name='menu'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    
]