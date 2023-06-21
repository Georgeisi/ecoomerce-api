from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .Serializer import product_serializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser




# Create your views here.
@api_view(['GET'])
def allproducts(request):
    if request.method=='GET':
        product = Product.objects.all()
        serializer= product_serializer(product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def post_product(request):
    if request.method=='POST':
        product= request.data
        serializer=product_serializer(data=product, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'product sucessfully added',
                'status': True
            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message':'something went wrong',
                'status': False
            },status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def Edit_product(request,id):
     if request.method=='GET':
        product = Product.objects.get(id=id)
        serializer= product_serializer(product, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
     elif request.method=='PUT':
        product= Product.objects.get(id=id)
        serializer= product_serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'product updated',
                'status': True
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message':'something went wrong',
                'status': False
            }, status=status.HTTP_400_BAD_REQUEST)
     elif request.method=='DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return Response({
            'message': 'product sucessfully deleted',
            'status': True
        }, status=status.HTTP_200_OK)

