from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dog(request):
    msg = "<h1>Dog</h1>"
    return render(request, 'dog/index.html')
