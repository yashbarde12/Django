from django.urls import path
from cafe import views

urlpatterns = [
    path('home/', views.homepage),

]