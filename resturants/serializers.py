from rest_framework import serializers
from .models import Resturant, Deal

class ResturantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resturant
        fields = '__all__'