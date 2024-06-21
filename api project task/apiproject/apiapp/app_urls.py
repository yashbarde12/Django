
from django.urls import path

from apiapp import views

urlpatterns = [
    path('user/', views.Userdetails.as_view()),
]