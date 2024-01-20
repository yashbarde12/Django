from django.shortcuts import render
from customer import models
from customer import forms
# Create your views here.
def view_customer(request):
    data = models.Customer.objects.all()
    all_customers = {'customers': data}
    return render(request, 'customer/view_customer.html', context= all_customers)

def register_customer(request):
    registration_form = forms.CustomerForm()
    form = {'form': registration_form}
    if (request.method == 'POST'):
        form_data = forms.CustomerForm(request.POST)
        if (form_data.is_valid()):
            form_data.save(commit=True)
            return view_customer(request)
    return render(request, 'customer/register_customer.html', context= form)
    
