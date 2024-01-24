
from django.shortcuts import render
from django.http import HttpResponse
import product
from product.models import Producttable
from product import forms
# Create your views here.
def view_product(request):
    result = Producttable.objects.all()
    print(result)
    data = {'product_list': result}
    return render (request, 'product/view_product.html', context= data)


def add_product(request):
    form = forms.ProductForm()
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if (form.is_valid()):
            obj = Producttable()
            obj.name = form.cleaned_data['name']
            obj.price = form.cleaned_data['price']
            obj.save()
            return view_product(request)
    
    data = {'product_form': form}
    return render(request, 'product/add_product.html', context= data)