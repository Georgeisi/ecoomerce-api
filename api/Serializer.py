from .models import Product
from rest_framework import serializers

class product_serializer(serializers.ModelSerializer):
    image= serializers.ImageField(required= False)

    class Meta:
        model= Product
        fields = '__all__'