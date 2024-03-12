from django.shortcuts import render, get_object_or_404
from menu.models import MenuItem
from django.db.models import Q
# Create your views here.
# menu/views.py


def menu(request):
    items = MenuItem.objects.all()

    # Handle search query
    query = request.GET.get('q')
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {
        'items': items,
        'query': query,
    }
    return render(request, 'menu/menu.html', context)

def filter_by_category(request, category):
    items = MenuItem.objects.filter(category=category)
    context = {
        'items': items,
        'category': category,
    }
    return render(request, 'menu/menu.html', context)

def filter_by_price_range(request, min_price, max_price):
    items = MenuItem.objects.filter(price__gte=min_price, price__lte=max_price)
    context = {
        'items': items,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'menu/menu.html', context)


def item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    context = {'item': item}
    return render(request, 'menu/item_detail.html', context)

