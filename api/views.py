from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from api.models import OrderModel, ProductModel, UserModel, CategoryModel
from api.serializers import OrderModelSerializer, ProductModelSerializer, UserModelSerializer, CategoryModelSerializer


class CategoryModelListAPIView(ListAPIView):
	queryset = CategoryModel.objects.all()
	serializer_class = CategoryModelSerializer


class OrderListAPIView(ListAPIView):
	serializer_class = OrderModelSerializer

	def get_queryset(self):
		pk = self.kwargs.get('pk')

		return OrderModel.objects.filter(user_id=pk)


class ProductModelListAPIView(ListAPIView):
	serializer_class = ProductModelSerializer

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		q = self.request.GET.get('q')

		if q:
			return ProductModel.objects.filter(title__icontains=q)
		elif pk:
			return ProductModel.objects.filter(category_id=pk)
		else:
			return ProductModel.objects.none()


class ProductModelRetrieveAPIView(RetrieveAPIView):
	serializer_class = ProductModelSerializer
	queryset = ProductModel.objects.all()


class OrderModelCreateAPIView(CreateAPIView):
	queryset = OrderModel.objects.all()
	serializer_class = OrderModelSerializer


class UserModelListAPIView(ListAPIView):
	serializer_class = UserModelSerializer

	def get_queryset(self):
		pk = self.kwargs.get('pk')

		return UserModel.objects.filter(tg_id=pk)


class UserModelCreateAPIView(CreateAPIView):
	serializer_class = UserModelSerializer
