from django.urls import path

from pilotapp import views

urlpatterns = [
    path('products/',views.list_products),
    path('products/<int:id>',views.product_detail),
    path('orders/',views.list_orders),
    path('orders/<int:id>',views.order_detail),
]