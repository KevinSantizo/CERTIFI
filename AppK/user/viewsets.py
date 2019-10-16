from rest_framework import viewsets
from user.models import Customer
from user.serializer import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
