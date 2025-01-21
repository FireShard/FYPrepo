from rest_framework import serializers
from .models import RamDetails, LaptopDetails, UserLaptop

class RamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamDetails
        fields = '__all__'  # Include all fields from the model

class LaptopDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopDetails
        fields = '__all__'

class UserLaptopSerializer(serializers.ModelSerializer):
    ram = RamDetailsSerializer(read_only=True)  # Nest the RamDetailsSerializer
    laptop = LaptopDetailsSerializer(read_only=True)  # Nest the LaptopDetailsSerializer
    ram_id = serializers.PrimaryKeyRelatedField(queryset=RamDetails.objects.all(), source='ram', write_only=True, allow_null=True) # For write operations
    laptop_id = serializers.PrimaryKeyRelatedField(queryset=LaptopDetails.objects.all(), source='laptop', write_only=True) # For write operations

    class Meta:
        model = UserLaptop
        fields = '__all__'
        #fields = ['userid', 'manufacturer', 'brand', 'productLine', 'CPU', 'GPU', 'ramSize', 'ramType', 'ram', 'laptop', 'ram_id', 'laptop_id'] # Example if you needed to specify fields explicitly