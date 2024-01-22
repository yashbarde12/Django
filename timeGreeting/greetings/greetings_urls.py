from django.urls import path
from greetings import views

urlpatterns = [
    path('home/', views.greeting_view),
]
