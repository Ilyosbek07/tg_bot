from django.contrib import admin

from api.models import OrderModel, UserModel, CategoryModel, ProductModel


@admin.register(OrderModel)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title']


@admin.register(UserModel)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'created_at']
	list_filter = ['created_at']
	search_fields = ['first_name']


@admin.register(ProductModel)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title']


@admin.register(CategoryModel)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title']
