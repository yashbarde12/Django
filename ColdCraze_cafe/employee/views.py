from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def emp_register(request):
    data = {}
    if request.method == "POST":
        emp_name = request.POST['username']
        emp_pass = request.POST['password']
        ucon_pass = request.POST['password2']
        if(emp_name == '' or emp_pass == '' or ucon_pass == ''):
            data['error_msg']='Field cannot be empty'
            return render(request, 'employee/emp_register.html', context=data)
        elif (emp_pass != ucon_pass):
            data['error_msg']='Password and confirm password does not match'
            return render(request, 'employee/emp_register.html', context=data)
        elif (User.objects.filter(username=emp_name)).exists():
            data['error_msg']=emp_name+' already exist'
            return render(request, 'employee/emp_register.html', context=data)
        else:
            user = User.objects.create(username=emp_name)
            user.set_password(emp_pass)
            user.save()
            # return HttpResponse('Registration done')
            return redirect('/employee/login')
    return render(request, 'employee/emp_register.html')

def emp_login(request):
    data = {}
    if request.method == 'POST':
        emp_name = request.POST['username']
        emp_pass = request.POST['password']
        if (emp_name=='' or emp_pass ==''):
            data['error_msg']='Fileds cant be empty'
            return render(request,'employee/emp_login.html',context=data)
        elif(not User.objects.filter(username=emp_name).exists()):
            data['error_msg']=emp_name + ' user is not registered'
            return render(request,'employee/emp_login.html',context=data)
        else:
            user=authenticate(username=emp_name,password=emp_pass)
            if user is not None:
                login(request, user)
                return redirect('/cafe/home')
            else:
                data['error_msg']='Wrong Password'
                return render(request,'employee/emp_login.html',context=data)   
    return render(request,'employee/emp_login.html')


def emp_logout(request):
    logout(request)
    return redirect('/employee/login')