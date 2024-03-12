from django.urls import path
from core.views import home

# core/urls.py

urlpatterns = [
    path('', home, name='home'),
]
