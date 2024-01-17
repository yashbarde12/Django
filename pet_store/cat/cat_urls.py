from django.urls import path
from cat import views

urlpatterns = [
    path('home/', views.cat),
]