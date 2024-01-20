from django.urls import path
from customer import views

urlpatterns = [
    path('view/', views.view_customer),
    path('register/', views.register_customer),
]