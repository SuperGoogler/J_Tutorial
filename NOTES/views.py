from rest_framework import generics, permissions
from .serializers import BookSerializers
from .models import Books

class BooksSerializerView(generics.GenericAPIView):
    serializer_class = BookSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Books.objects.all()

    # def get_queryset(self, *args, **kwargs):
    #     return self.get_queryset()
