from rest_framework import serializers
from ekartApp.models import Product,Category,Cart,Order,Review
from django.contrib.auth.models import User


class ProductSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    total_rating=serializers.FloatField(read_only=True)
    class Meta:
        model=Product
        fields="__all__"



class UserSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","password"]

class CartSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    product_instance=ProductSerialiser(read_only=True)
    user_instance=UserSerialiser(read_only=True)
    class Meta:
        model=Cart
        fields="__all__"

class OrderSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    user_instance=UserSerialiser(read_only=True)
    cart_instance=CartSerialiser(read_only=True)
    class Meta:
        model=Order
        fields="__all__"

class ReviewSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    user_instance=UserSerialiser(read_only=True)
    product_instance=ProductSerialiser(read_only=True)
    class Meta:
        model=Review
        fields="__all__"