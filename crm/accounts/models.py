from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user  = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profil_pic = models.ImageField(null=True, blank=True, default='user_default.webp')
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name if self.name else "Unnamed Customer"

class Tag(models.Model):
	name = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return self.name
	
class Product(models.Model):

	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True) 
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name
	

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			) 

	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.product)
