from django.contrib import admin

from api.models import OrderModel, UserModel, CategoryModel, ProductModel

admin.site.register(OrderModel)
admin.site.register(ProductModel)
admin.site.register(UserModel)
admin.site.register(CategoryModel)


