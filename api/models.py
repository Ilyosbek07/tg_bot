from django.db import models


# from ckeditor_uploader.fields import RichTextUploadingField
class CategoryModel(models.Model):
	title = models.CharField(max_length=55)
	created_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class UserModel(models.Model):
	tg_id = models.IntegerField(unique=True)
	user_name = models.CharField(max_length=75)
	first_name = models.CharField(max_length=75, null=True, blank=True)
	last_name = models.CharField(max_length=75, null=True, blank=True)
	number = models.CharField(max_length=75)
	address = models.CharField(max_length=75)
	created_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.user_name

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'


class ProductModel(models.Model):
	title = models.CharField(max_length=55)
	image = models.ImageField(null=True)
	price = models.IntegerField()
	description = models.TextField(null=True)
	category = models.ForeignKey(
		CategoryModel,
		on_delete=models.CASCADE,
		related_name='products'
	)
	created_at = models.DateField(auto_now_add=True)

	# description = RichTextUploadingField()
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'


class OrderModel(models.Model):
	product_id = models.IntegerField(unique=True)
	user_id = models.IntegerField(unique=True)
	user = models.CharField(max_length=255)
	title = models.CharField(max_length=55)
	price = models.IntegerField()
	number = models.CharField(max_length=55)
	address = models.CharField(max_length=255)

	created_at = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'
