from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.views.generic import DetailView, TemplateView

from mainapp.mixin import BaseClassContentMixin
from mainapp.models import Product, ProductCategory

class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'

# def index(request):
#     context = {
#         'title': 'geekshop',
#     }
#     return render(request, 'mainapp/index.html', context)

def products(request, id_category=None, page=1):

    context = {
        'title': 'geekshop - Каталог',
    }

    if id_category:
        products=Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()

    paginator=Paginator(products, per_page=3)

    try:
        products_paginator= paginator.page(page)
    except PageNotAnInteger:
        products_paginator= paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    context['categories']=ProductCategory.objects.all()

    return render(request, 'mainapp/products.html', context)


class ProductDetailView(DetailView, BaseClassContentMixin):
    model = Product
    template_name = 'mainapp/product.html'
    title = 'geekshop - Подробное описание'