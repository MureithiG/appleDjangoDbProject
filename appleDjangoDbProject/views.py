from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def add_products(request):
    if request.method == "POST":
        product_name = request.POST.get('p-name')
        product_qtty = request.POST.get('p-qtty')
        product_price = request.POST.get('p-price')
        product_desc = request.POST.get('p-desc')

        data = Product(name=product_name, qtty=product_qtty, price=product_price, desc=product_desc)
        data.save()
        messages.success(request, 'Product added successfully')
        return redirect('add-products-url')
    return render(request, 'add-products.html')
