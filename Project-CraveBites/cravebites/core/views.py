from django.shortcuts import render

# Create your views here.
# core/views.py

def home(request):
    return render(request, 'core/home.html')