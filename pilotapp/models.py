from django.db import models
from django.db.models import Sum
import datetime
# Create your models here.
class Tag(models.Model):
    tag_name = models.TextField()
#commect to check branch
class Category(models.Model):
    category_name = models.TextField()
    description = models.TextField()
    #img

class Product(models.Model):
    product_name = models.TextField()
    price = models.IntegerField()
    description=models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

class Order(models.Model):
    order_items= models.ManyToManyField(Product,through="OrderItem")
    order_time = datetime.time()
    total_cost = models.FloatField(default=0)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    instruction = models.TextField()

    def __str__():
        return f"Order Id : {id}"


        



  




