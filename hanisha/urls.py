from django.urls import path
from django.contrib.auth import views as auth_views

from hanisha import views

urlpatterns = [
    # URL for the list view of items
    path('item_list/', views.item_list, name='item_list'),

    # URL for adding a new item
    path('add_item/', views.add_item, name='add_item'),

    # URL for viewing a specific item (you can pass the item ID as a parameter)
    path('items/<int:item_id>/', views.view_items, name='view_items'),

    # URL for updating a specific item (you can pass the item ID as a parameter)
    path('item_list/<int:item_id>/', views.edit_item, name='edit_item'),

    # URL for deleting a specific item (you can pass the item ID as a parameter)
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('', views.home, name='home')
]
