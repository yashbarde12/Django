from django.shortcuts import render
import datetime
# Create your views here.

def greeting_view(request):
    current_time = datetime.datetime.now().time()

    if datetime.time(6, 0) <= current_time < datetime.time(12, 0):
        greeting = 'Good morning.'
    elif datetime.time(12, 0) <= current_time < datetime.time(18, 0):
        greeting = 'Good afternoon.'
    else:
        greeting = 'Good evening.'

    return render(request, 'greetings/index.html', {'current_time':current_time ,'greeting': greeting})
