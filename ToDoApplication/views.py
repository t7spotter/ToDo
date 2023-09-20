from rest_framework import generics

from .models import todo
from .serializers import TodoSerializers


class TodoView(generics.ListCreateAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoSerializers
    
    
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoSerializers