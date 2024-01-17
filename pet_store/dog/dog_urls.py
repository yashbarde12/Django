from django.urls import path
from dog import views

urlpatterns = [
    path('home/', views.dog),
]