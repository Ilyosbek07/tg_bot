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
	user_name = models.CharField(max_length=75, unique=True, null=True, blank=True)
	first_name = models.CharField(max_length=75)
	last_name = models.CharField(max_length=75, null=True, blank=True)
	number = models.CharField(max_length=75)
	address = models.CharField(max_length=75, null=True, blank=True)
	created_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.user_name} ({self.first_name}) | {self.last_name}'

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
	address = models.CharField(max_length=255, null=True)
	soni = models.CharField(max_length=55)
	TASDIQLANDI = 'TASDIQLANDI'
	TASDIQLANMADI = 'TASDIQLANMADI'
	Xolati = [
		(TASDIQLANDI, 'Tasdiqlandi'),
		(TASDIQLANMADI, 'tASDIQLANMADI'),
	]
	order = models.CharField(
		max_length=255,
		choices=Xolati,
		default=TASDIQLANMADI,
	)
	created_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'
