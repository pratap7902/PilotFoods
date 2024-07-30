import graphene
from graphene_django import DjangoObjectType
from .models import Tag, Category, Product, Order, OrderItem

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





class CreateTag(graphene.Mutation):
    tags = graphene.Field(TagType)

    class Arguments:
        tag_name = graphene.String(required=True)

    def mutate(self, info, tag_name):
        tags = Tag(tag_name=tag_name)
        tags.save()

        return CreateTag(tags=tags)


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


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_tag = CreateTag.Field()
    create_product = CreateProduct.Field()






schema = graphene.Schema(query=Query,mutation=Mutation)