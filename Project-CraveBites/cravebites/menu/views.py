from django.shortcuts import render, get_object_or_404
from menu.models import MenuItem
# Create your views here.
# menu/views.py


def menu(request):
    items = MenuItem.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        items = items.filter(name__icontains=query)

    context = {'items': items, 'query': query}
    return render(request, 'menu/menu.html', context)


def item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    context = {'item': item}
    return render(request, 'menu/item_detail.html', context)

