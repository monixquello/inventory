from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.shortcuts import get_object_or_404

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list page
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


def view_items(request,item_id):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('item_list')

def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)  # Retrieve the item by its ID
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list page
    else:
        form = ItemForm(instance=item)  # Populate the form with item data
    return render(request, 'edit_item.html', {'form': form, 'item': item})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def home(request):
    # Retrieve a list of spare parts from the database
    item_list = Item.objects.all()  # You may need to adjust this query

    # Render the template and pass the data
    return render(request, 'home.html', {'products': item_list})
