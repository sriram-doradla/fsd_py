# from django.shortcuts import render
# from .models import Product
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import ProductSerializer, UserRegistrationSerializer
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib import messages

# def home(request):
#     products = Product.objects.all()
#     context = {
#         'products' : products
#     }
#     return render(request, 'website/index.html', context)


# def search(request):
#     query = request.GET.get("q")
#     products = Product.objects.filter(productname__icontains=query) if query else []
#     return render(request, 'website/index.html', {"search": query, "products": products})

# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect("home")  # change to your homepage
#         else:
#             messages.error(request, "Invalid username or password")
#     return render(request, "website/login.html")


# def logout(request):
#     return render(request, 'website/logout.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .models import Product
from .serializers import ProductSerializer, UserRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'website/index.html', context)


def search(request):
    query = request.GET.get("q")
    products = Product.objects.filter(productname__icontains=query) if query else []
    return render(request, 'website/index.html', {"search": query, "products": products})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "website/login.html")


def logout(request):
    auth_logout(request)
    return redirect("login")


# @api_view(['GET'])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def add_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def update_product(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     serializer = ProductSerializer(product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_product(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     product.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST'])
# def register_user(request):
#     serializer = UserRegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
