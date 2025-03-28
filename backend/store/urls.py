from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),  # List and create items
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),  # Retrieve, update, and delete a single item
]
