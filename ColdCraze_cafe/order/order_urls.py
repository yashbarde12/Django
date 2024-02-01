from django.urls import path
from order import views

urlpatterns = [
    path('view/', views.view_order),
    path('add/', views.add_order),
    path('delete/<int:orderid>', views.delete_order),
    path('update/<int:orderid>', views.update_order),
]