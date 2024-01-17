from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cat(request):
    msg = "<h1>Cat</h1>"
    return render(request, 'cat/index.html')