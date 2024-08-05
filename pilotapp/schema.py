import datetime
import graphene
from graphene_django import DjangoObjectType
from .models import Tag, Category, Product, Order, OrderItem


# Schema Definition for Tag Model

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')

# Schema Definition for Category Model

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'description')

# Schema Definition for Product Model

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'price', 'description', 'category', 'tag')


# Schema Definition for OrderItem Model

class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'instruction')


# Schema Definition for Orders Model

class Orders(DjangoObjectType):
    class Meta:
        model = Order
        fields = ('id', 'order_items', 'order_time', 'total_cost')



    def resolve_order_items(self, info):        # resolving each order item associated with the order
        return self.order_items.all()



# Querries for all models
class Query(graphene.ObjectType):
    tags = graphene.List(TagType)
    categories = graphene.List(CategoryType)
    products = graphene.List(ProductType)
    orders = graphene.List(Orders)

    def resolve_tags(self, info):
        return Tag.objects.all()

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_orders(self, info):
        return Order.objects.all()




# Mutation to create a Tag

class CreateTag(graphene.Mutation):
    tags = graphene.Field(TagType)

    class Arguments:
        tag_name = graphene.String(required=True)

    def mutate(self, info, tag_name):
        tags = Tag(tag_name=tag_name)
        tags.save()

        return CreateTag(tags=tags)







# Mutation to create a Product



class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        product_name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        description = graphene.String(required=True)
        category_name = graphene.String(required=True)
        tag_names = graphene.List(graphene.String, required=True)

    def mutate(self, info, product_name, price, description, category_name, tag_names):
        try:
            category = Category.objects.get(category_name=category_name)
        except Category.DoesNotExist:
            raise Exception("Category does not exist")

        tags = []
        for tag_name in tag_names:
            try:
                tag = Tag.objects.get(tag_name=tag_name)
            except Tag.DoesNotExist:
                tag = Tag(tag_name=tag_name)
                tag.save()
            tags.append(tag)

        product = Product(product_name=product_name, price=price, description=description, category=category)
        product.save()
        product.tag.set(tags)

        return CreateProduct(product=product)



class CreateCategory(graphene.Mutation):
    category=graphene.Field(CategoryType)

    class Arguments:
        category_name = graphene.String(required=True)
        description = graphene.String(required=True)
        

    def mutate(self, info, category_name,description):
        
        category= Category(category_name=category_name,description=description)
        category.save()

        return CreateCategory(category=category)



# properties required to define a product in a order
#Note- product_id and quantity are required fields
class OrderItemInput(graphene.InputObjectType):
    product_id = graphene.ID(required=True)
    quantity = graphene.Int(required=True)
    instruction = graphene.String(default="Null")




#Mutation to create an order
class CreateOrder(graphene.Mutation):
    order = graphene.Field(Orders)

    class Arguments:
        order_items = graphene.List(OrderItemInput)

    def mutate(self, info, order_items):
        
        total_cost = 0

        order = Order()
        

        for item in order_items:
            product = Product.objects.get(id=item.product_id)
            order_item = OrderItem(order=order, product=product, quantity=item.quantity, instruction=item.instruction)
            order_item.save()
            total_cost += product.price * item.quantity

        order.total_cost = total_cost
        order.save()

        return CreateOrder(order=order)







#Mutation class
class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_tag = CreateTag.Field()
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()






schema = graphene.Schema(query=Query,mutation=Mutation)