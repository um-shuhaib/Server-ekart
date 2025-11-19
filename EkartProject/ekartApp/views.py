from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ekartApp.models import Category,Product,Cart
from rest_framework.response import Response
from ekartApp.serialisers import ProductSerialiser,CartSerialiser
from rest_framework.decorators import action
from rest_framework import permissions,authentication

# Create your views here.
class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerialiser

    #custom method for create()
    # baseurl/p_id/add_to_cart - http://127.0.0.1:8000/1/add_to_cart
    @action(methods=["POST"],detail=True,authentication_classes=[authentication.TokenAuthentication],permission_classess=[permissions.IsAuthenticated])
    def add_to_cart(self,request,*args,**kwargs):
        user=request.user
        product=Product.objects.get(id=kwargs.get("pk"))
        serialisation=ProductSerialiser(data=request.data)
        if serialisation.is_valid():
            Cart.objects.create(**serialisation.validated_data,user_instance=user,product_instance=product)
            return Response(data=serialisation.data)


# class CartView(ModelViewSet):
#     queryset=Cart.objects.all()
#     serializer_class=CartSerialiser

# we cant do because cant get the pro id so above method


    