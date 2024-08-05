from django.db import models
from django.db.models import Sum
import datetime



# Tag Model
class Tag(models.Model):
    tag_name = models.TextField()


# Category Model
class Category(models.Model):
    category_name = models.TextField()
    description = models.TextField()

# Product Model
class Product(models.Model):
    product_name = models.TextField()
    price = models.IntegerField()
    description=models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


# Order Model
class Order(models.Model):
    order_items= models.ManyToManyField(Product,through='OrderItem')
    order_time = models.DateTimeField(default=datetime.datetime.now())
    total_cost = models.FloatField(default=0)


#Order Item Model (Contains each product associated with a particular order)
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)    
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    instruction = models.TextField()

    def __str__():
        return f"Order Id : {id} "


        



  




