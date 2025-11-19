from rest_framework import serializers
from ekartApp.models import Product,Category,Cart


class ProductSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Product
        fields="__all__"

class CartSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    product_instance=serializers.CharField(read_only=True)
    user_instance=serializers.CharField(read_only=True)
    class Meta:
        model=Cart
        fields="__all__"