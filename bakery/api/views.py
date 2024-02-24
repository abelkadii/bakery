from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from sales.models import *

# Create your views here.

# /api/products
@api_view(['GET'])
def products(request):
    filters = ['price', 'category', 'priceMax', 'priceMin']
    products=Product.objects.all()
    # apply filters
    for filter in filters:
        if filter in request.GET:
            if filter == 'price':
                products = products.filter(price=request.GET[filter])
            elif filter == 'category':
                products = products.filter(category=request.GET[filter])
            elif filter == 'priceMax':
                products = products.filter(price__lte=request.GET[filter])
            elif filter == 'priceMin':
                products = products.filter(price__gte=request.GET[filter])
    if not products:
        return Response({'error':'No products found'}, status=404)
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

# /api/products/id
@api_view(['GET'])
def product(request, pk):
    products=Product.objects.all().filter(id=pk)
    if not products:
        return Response({'error':'Product not found'}, status=404)
    serializer=ProductSerializer(products[0])
    return Response(serializer.data)

# /api/orders
@api_view(['GET'])
def orders(request):
    filters = ['product', 'quantity', 'day', 'dayMax', 'dayMin', 'total', 'totalMax', 'totalMin'] 
    # apply filters
    orders = Order.objects.all()
    for filter in filters:
        if filter in request.GET:
            if filter == 'product':
                orders = orders.filter(product=request.GET[filter])
            elif filter == 'quantity':
                orders = orders.filter(quantity=request.GET[filter])
            elif filter == 'day':
                orders = orders.filter(day=request.GET[filter])
            elif filter == 'dayMax':
                orders = orders.filter(day__lte=request.GET[filter])
            elif filter == 'dayMin':
                orders = orders.filter(day__gte=request.GET[filter])
            elif filter == 'total':
                orders = orders.filter(total=request.GET[filter])
            elif filter == 'totalMax':
                orders = orders.filter(total__lte=request.GET[filter])
            elif filter == 'totalMin':
                orders = orders.filter(total__gte=request.GET[filter])
    if not orders:
        return Response({'error':'No orders found'}, status=404)
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

# /api/order/id
@api_view(['GET'])
def order(request, pk):
    orders=Order.objects.all().filter(id=pk)
    if not orders:
        return Response({'error':'Order not found'}, status=404)
    serializer=OrderSerializer(orders[0])
    return Response(serializer.data)

# /api/product/id/sell {quantity: int}
@api_view(['POST'])
def sell(request, pk):
    products=Product.objects.all().filter(id=pk)
    if not products:
        return Response({'error':'Product not found'}, status=404)
    if 'quantity' not in request.data:
        return Response({'error':'Quantity not provided'}, status=400)
    if products[0].stock < request.data['quantity']:
        return Response({'error':'Not enough stock'}, status=400)
    products[0].stock -= request.data['quantity']
    products[0].save()
    order = Order.objects.create(product=products[0], quantity=request.data['quantity'], total=products[0].price*request.data['quantity'])
    serializer=OrderSerializer(order)
    return Response(serializer.data)

# /api/product/id/restock {quantity: int}
@api_view(['POST'])
def restock(request, pk):
    products=Product.objects.all().filter(id=pk)
    if not products:
        return Response({'error':'Product not found'}, status=404)
    if 'quantity' not in request.data:
        return Response({'error':'Quantity not provided'}, status=400)
    products[0].stock += request.data['quantity']
    products[0].save()
    restock = Restock.objects.create(product=products[0], quantity=request.data['quantity'])
    serializer=ProductSerializer(products[0])
    return Response(serializer.data)