from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ekartApp.models import Category,Product,Cart,Order,Review
from rest_framework.response import Response
from ekartApp.serialisers import ProductSerialiser,CartSerialiser,UserSerialiser,OrderSerialiser,ReviewSerialiser
from rest_framework.decorators import action
from rest_framework import permissions,authentication
from django.contrib.auth.models import User

# Create your views here.
class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerialiser

    #custom method for create()
    # baseurl/p_id/add_to_cart - http://127.0.0.1:8000/product/1/add_to_cart
    @action(methods=["POST"],detail=True,authentication_classes=[authentication.TokenAuthentication],permission_classes=[permissions.IsAuthenticated])
    def add_to_cart(self,request,*args,**kwargs):
        user=request.user
        product=Product.objects.get(id=kwargs.get("pk"))
        serialisation=CartSerialiser(data=request.data)
        if serialisation.is_valid():
            Cart.objects.create(**serialisation.validated_data,user_instance=user,product_instance=product)
            return Response({"msg":"product added to cart"})
        
    @action(methods=["POST"],detail=True,authentication_classes=[authentication.TokenAuthentication],permission_classes=[permissions.IsAuthenticated])  
    def add_review(self,request,*args,**kwargs):
        try:
            product=Product.objects.get(id=kwargs.get("pk"))
            user=request.user
            serialiser=ReviewSerialiser(data=request.data)
            if serialiser.is_valid():
                try:
                    Review.objects.create(**serialiser.validated_data,user_instance=user,product_instance=product) # we can also use getorcreate (then we dont need the unique group in model )
                    return Response(data=serialiser.data)
                except:
                    return Response({"msg":"comment already added"})
        except:
            return Response({"msg":"matching qoury does not exist"})

    @action(methods=["GET"],detail=True)  
    def review_list(self,request,*args,**kwargs):
        product=Product.objects.get(id=kwargs.get("pk"))
        reviews=Review.objects.filter(product_instance=product)
        serialiser=ReviewSerialiser(reviews,many=True)
        return Response(data=serialiser.data)
       



# class CartView(ModelViewSet):
#     queryset=Cart.objects.all()
#     serializer_class=CartSerialiser

# we cant do because cant get the pro id so above method

class UserView(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerialiser

    def create(self, request, *args, **kwargs):
        serialiser=UserSerialiser(data=request.data)
        if serialiser.is_valid():
            User.objects.create_user(**serialiser.validated_data)
            return Response(data=serialiser.data)
        else:
            return Response(data=serialiser.errors)
    # http://127.0.0.1:8000/user/1/cart_list
    @action(methods=["GET"],detail=True)    
    def cart_list(self,request,*args,**kwargs):
        user=User.objects.get(id=kwargs.get("pk"))
        cart=Cart.objects.filter(user_instance=user)
        serialiser=CartSerialiser(cart,many=True)
        return Response(data=serialiser.data)
    
class CartView(ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerialiser

    @action(methods=["POST"],detail=True,authentication_classes=[authentication.TokenAuthentication],permission_classes=[permissions.IsAuthenticated])
    def place_order(self,request,*args,**kwargs):
        cart=Cart.objects.get(id=kwargs.get("pk"))
        user=request.user
        serialiser=OrderSerialiser(data=request.data)
        if serialiser.is_valid():
            Order.objects.create(**serialiser.validated_data,user_instance=user,cart_instance=cart)
            cart.status="order-places"
            cart.save()
            return Response({"msg":"order places"})
        else:
            return Response(data=serialiser.errors)


