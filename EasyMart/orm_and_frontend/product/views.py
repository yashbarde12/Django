from django.shortcuts import render
from django.http import HttpResponse
from product.models import CartTable, ProductTable
from django.db.models import Q

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
   data={}
   #ProductTable.objects.all() this will fetch non active product also. so it is better to use filter
   fetched_products=ProductTable.objects.filter(is_active=True)
   data['products']=fetched_products
   return render(request,'product/index.html',context=data)

def filter_by_category(request,category_value):
   #select * from product where is_active=True and category=category_value;
   #ProductTable.objects.filter(is_active=True , category=category_value)
   #from django.db.models import Q
   data={}
   q1 = Q(is_active=True)
   q2 = Q(category=category_value)
   filterd_products=ProductTable.objects.filter(q1 & q2)
   data['products']=filterd_products
   return render(request,'product/index.html',context=data)

def sort_by_price(request,sort_value):
   #select * from product order by salary desc;
   data={}
   if sort_value=='asc':
      price = 'price'
   else:
      price = '-price'
   sorted_products=ProductTable.objects.filter(is_active=True).order_by(price)
   data['products']=sorted_products
   return render(request,'product/index.html',context=data)

def filter_by_rating(request,rating_value):
   #select * from product where is_active=True and category=category_value;
   #ProductTable.objects.filter(is_active=True , category=category_value)
   #from django.db.models import Q
   data={}
   q1 = Q(is_active=True)
   q2 = Q(rating__gt=rating_value)
   filterd_products=ProductTable.objects.filter(q1 & q2)
   data['products']=filterd_products
   return render(request,'product/index.html',context=data)


def filter_by_price_range(request):
   data={}
   min = request.GET['min']
   max = request.GET['max']
   q1 = Q(price__gte=min)
   q2 = Q(price__lte=max)
   q3 = Q(is_active=True)
   filterd_products=ProductTable.objects.filter(q1 & q2 & q3)
   data['products']=filterd_products
   return render(request,'product/index.html',context=data)

def product_detail(request, pid):
   product = ProductTable.objects.get(id=pid)
   return render(request, 'product/product_detail.html', {'product': product})

#----------------------user registration and login---------------------------
def register_user(request):
    data = {}
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        ucon_pass = request.POST['password2']
        if(uname == '' or upass == '' or ucon_pass == ''):
            data['error_msg']='Field cannot be empty'
            return render(request, 'user/register.html', context=data)
        elif (upass != ucon_pass):
            data['error_msg']='Password and confirm password does not match'
            return render(request, 'user/register.html', context=data)
        elif (User.objects.filter(username=uname)).exists():
            data['error_msg']=uname+' already exist'
            return render(request, 'user/register.html', context=data)
        else:
            user = User.objects.create(username=uname)
            user.set_password(upass)
            user.save()
            # return HttpResponse('Registration done')
            return redirect('/user/login')
    return render(request, 'user/register.html')

def login_user(request):
    data = {}
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        if (uname=='' or upass ==''):
            data['error_msg']='Fileds cant be empty'
            return render(request,'user/login.html',context=data)
        elif(not User.objects.filter(username=uname).exists()):
            data['error_msg']=uname + ' user is not registered'
            return render(request,'user/login.html',context=data)
        else:
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                return redirect('/product/index')
            else:
                data['error_msg']='Wrong Password'
                return render(request,'user/login.html',context=data)   
    return render(request,'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('/product/index')

#----------------------cart---------------------------
def add_to_cart(request, pid):
    if request.user.is_authenticated:
        uid = request.user.id
        print("user id = ", uid)
        print("product id = ", pid)
        user = User.objects.get(id=uid)
        product = ProductTable.objects.get(id=pid)
        cart = CartTable.objects.create(pid=product, uid=user)
        cart.save()
        return HttpResponse("Product added to cart")
    else:
        return redirect("/user/login")

def view_cart(request):
    cart_items = CartTable.objects.filter(user=request.user.id)
    context = {'cart_items': cart_items}
    return render(request, 'product/view_cart.html', context)