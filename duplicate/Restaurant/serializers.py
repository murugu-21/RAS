from rest_framework import serializers
from .models import *

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('item_code','ingredient_list_id', 'quantity_list', 'price', 'name')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('email', 'type', 'password', 'otp')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('ingredient_id', 'name', 'quantity', 'thresholdvalue')

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('item_code', 'quantity', 'date')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('ingredient', 'quantity', 'price', 'date')

class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = ('balance')