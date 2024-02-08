from django.shortcuts import render, redirect
from order import models
from order import forms
import order
# Create your views here.

def view_order(request):
    data = models.Order.objects.all()
    all_orders = {'orders': data}
    return render(request, 'order/view_order.html', context= all_orders)

def add_order(request):
    if (request.method == 'GET'):
        order_form = forms.OrderForm()
        form = {'form': order_form}
        return render(request, 'order/add_order.html', context= form)
    else:
        form_data = forms.OrderForm(request.POST)
        if (form_data.is_valid()):
            form_data.save(commit=True)
            return redirect("/order/view/")
    
def delete_order(request, orderid):
    order = models.Order.objects.get(id=orderid)
    order.delete()
    return redirect("/order/view/")

def update_order(request, orderid):
    order= models.Order.objects.get(id=orderid)
    data = {'customer': order}
    if (request.method == 'POST'):
        form_data = forms.OrderForm(request.POST, instance=order)
        print(form_data)
        if (form_data.is_valid()):
            form_data.save(commit=True)
            return redirect("/order/view/")
        else:
            print("Not Valid")
            print(form_data.errors)
            return redirect("/order/view/")
    return render(request, 'order/update_order.html', context= data)