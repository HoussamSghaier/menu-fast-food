from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# Create a view to list all items
class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Create a view to retrieve a single item
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
