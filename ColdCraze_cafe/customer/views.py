from django.shortcuts import render, redirect
from customer import models
from customer import forms
import customer
# Create your views here.
def view_customer(request):
    data = models.Customer.objects.all()
    all_customers = {'customers': data}
    return render(request, 'customer/view_customer.html', context= all_customers)

def register_customer(request):
    if (request.method == 'GET'):
        registration_form = forms.CustomerForm()
        form = {'form': registration_form}
        return render(request, 'customer/register_customer.html', context= form)
    else:
        form_data = forms.CustomerForm(request.POST)
        if (form_data.is_valid()):
            form_data.save(commit=True)
            return redirect("/customer/view/")
    
def delete_customer(request, customerid):
    customer = models.Customer.objects.get(id=customerid)
    customer.delete()
    return redirect("/customer/view/")

def update_customer(request, customerid):
    customer= models.Customer.objects.get(id=customerid)
    data = {'customer': customer}
    if (request.method == 'POST'):
        form_data = forms.CustomerForm(request.POST, instance=customer)
        print(form_data)
        if (form_data.is_valid()):
            form_data.save(commit=True)
            return redirect("/customer/view/")
        else:
            print("Not Valid")
            print(form_data.errors)
            return redirect("/customer/view/")
    return render(request, 'customer/update_customer.html', context= data)




    
