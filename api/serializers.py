from rest_framework import serializers

from api.models import UserModel, OrderModel, ProductModel, CategoryModel


class CategoryModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
	category = CategoryModelSerializer()

	class Meta:
		model = ProductModel
		fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'


class OrderModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderModel
		fields = '__all__'
