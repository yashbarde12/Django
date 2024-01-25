
from django.urls import path
from . import views

urlpatterns = [
    path('<str:lookup_field>/<str:lookup_type>/<str:search_term>/', views.employee_search, name='employee_search'),
]

