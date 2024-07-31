import graphene
from graphene_django import DjangoObjectType
from .models import Tag, Category, Product, Order, OrderItem
#check comment
class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'description')

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'price', 'description', 'category', 'tag')

class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'instruction')

class Order(DjangoObjectType):
    class Meta:
        model = Order
        fields = ('id', 'order_items', 'order_time', 'total_cost')

    order_items = graphene.List(OrderItemType)

    def resolve_order_items(self, info):
        return self.order_items.all()


class Query(graphene.ObjectType):
    tags = graphene.List(TagType)
    categories = graphene.List(CategoryType)
    products = graphene.List(ProductType)
    orders = graphene.List(Order)

    def resolve_tags(self, info):
        return Tag.objects.all()

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_orders(self, info):
        return Order.objects.all()

schema = graphene.Schema(query=Query)