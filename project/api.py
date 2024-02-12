from .models import Producto
from rest_framework import viewsets,permissions
from .serializers import productoSerializers

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = productoSerializers