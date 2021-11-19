from django.shortcuts import render, get_object_or_404


# Create your views here.
from mainapp.models import Product


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    product = Product.objects.all()
    context = {
        'title': 'geekshop - Каталог',
        'product': product

    }
    return render(request, 'mainapp/products.html', context)

