from django.shortcuts import render

import json 
import requests

from django.shortcuts import render        
from django.http import HttpResponse
from django.http import JsonResponse
from pilotapp.models import Product
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







def product(request,id):

    # url = 'http://localhost:8000/graphql/'


    # query = f"{{product(id: {id}) {{price,productName,description,category{{categoryName,}}}}}}"


    # response = requests.get(url, json={'query': query})

   
    # return JsonResponse(response.json()['data'])

    data = Product.objects.filter(pk=id).values()
    json_data = json.dumps(list(data))
    return HttpResponse(json_data, content_type='application/json')
