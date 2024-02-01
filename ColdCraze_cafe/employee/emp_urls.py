from django.urls import path
from employee import views

urlpatterns = [
    path('register/', views.emp_register),
    path('login/', views.emp_login),
    path('logout/', views.emp_logout),
]