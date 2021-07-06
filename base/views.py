from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .products import products


@api_view(["GET"])
def getRoutes(request):
    apis = ["api/products"]
    return Response(apis)


@api_view(["GET"])
def getProducts(request):
    return Response(products)
