from rest_framework import serializers
from ekartApp.models import Product,Category


class ProductSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Product
        fields="__all__"