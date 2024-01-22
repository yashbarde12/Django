from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def register_user(request):
    data = {}
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        ucon_pass = request.POST['password2']
        if(uname == '' or upass == '' or ucon_pass == ''):
            data['error_msg']='Field cannot be empty'
            return render(request, 'myapp/register.html', context=data)
        elif (upass != ucon_pass):
            data['error_msg']='Password and confirm password does not match'
            return render(request, 'myapp/register.html', context=data)
        elif (User.objects.filter(username=uname)).exists():
            data['error_msg']=uname+' already exist'
            return render(request, 'myapp/register.html', context=data)
        else:
            user = User.objects.create(username=uname)
            user.set_password(upass)
            user.save()
            return HttpResponse('Registration done')
    return render(request, 'myapp/register.html')

def login_user(request):
    data = {}
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        if (uname=='' or upass ==''):
            data['error_msg']='Fileds cant be empty'
            return render(request,'myapp/login.html',context=data)
        elif(not User.objects.filter(username=uname).exists()):
            data['error_msg']=uname + ' user is not registered'
            return render(request,'myapp/login.html',context=data)
        else:
            user=authenticate(username=uname,password=upass)
            if user is not None:
                return redirect('/myapp/home')
            else:
                data['error_msg']='Wrong Password'
                return render(request,'myapp/login.html',context=data)   
    return render(request,'myapp/login.html')

def home(request):
   return render(request,'myapp/home.html')