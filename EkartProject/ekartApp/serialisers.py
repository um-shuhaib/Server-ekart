from rest_framework import serializers
from ekartApp.models import Product,Category,Cart
from django.contrib.auth.models import User


class ProductSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
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