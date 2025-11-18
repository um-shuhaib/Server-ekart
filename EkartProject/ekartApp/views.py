from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ekartApp.models import Category,Product
from rest_framework.response import Response
from ekartApp.serialisers import ProductSerialiser

# Create your views here.
class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerialiser

    