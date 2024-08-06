from django.shortcuts import render

import json 
import requests

from django.shortcuts import render        
from django.http import HttpResponse
from django.http import JsonResponse
from pilotapp.models import Product, Order
from django.core import serializers



def list_products(request):
    
    # url = 'http://localhost:8000/graphql/'

   
    # query = """
    # {
    #   products {
    #     id
    #     category {
    #       categoryName
    #       description
    #     }
    #     price
    #     description
    #   }
    # }
    # """

   
    # response = requests.get(url, json={'query': query})

   
    # return JsonResponse(response.json()['data'])

    
    data = Product.objects.all().values()
    json_data = json.dumps(list(data))




    return HttpResponse(json_data, content_type='application/json')







def product_detail(request,id):

    # url = 'http://localhost:8000/graphql/'


    # query = f"{{product(id: {id}) {{price,productName,description,category{{categoryName,}}}}}}"


    # response = requests.get(url, json={'query': query})

   
    # return JsonResponse(response.json()['data'])

    data = Product.objects.filter(pk=id).values()
    json_data = json.dumps(list(data))
    return HttpResponse(json_data, content_type='application/json')





def list_orders(request):
       


    url = 'http://localhost:8000/graphql/'

   
    query = "query OrderAll {\n  orders {\n    id\n    products {\n      product {\n        productName\n        price\n        description\n        id\n        category {\n          description\n          categoryName\n          id\n        }\n        tag {\n          id\n          tagName\n        }\n      }\n      id\n      instruction\n      quantity\n    }\n    orderTime\n    totalCost\n  }\n}"

   
    response = requests.post(url, json={'query': query})

   
    return JsonResponse(response.json()['data'])


  
    # data = Order.objects.all().values()
    # json_data = json.dumps(list(data))

    # return HttpResponse(json_data, content_type='application/json')







def order_detail(request,id):

    data = Order.objects.filter(pk=id).values()
    json_data = json.dumps(list(data))
    return HttpResponse(json_data, content_type='application/json')
