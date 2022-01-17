from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.conf import settings
from django.core.cache import cache

# Create your views here.
from django.views.generic import DetailView, TemplateView

from mainapp.mixin import BaseClassContentMixin
from mainapp.models import Product, ProductCategory

def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()

def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')

def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)

class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'

# def index(request):
#     context = {
#         'title': 'geekshop',
#     }
#     return render(request, 'mainapp/index.html', context)


# @cache_page(3600)
# @never_cache
def products(request, id_category=None, page=1):

    context = {
        'title': 'geekshop - Каталог',
    }

    if id_category:
        products=Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()

    products = get_link_product()

    paginator=Paginator(products, per_page=3)

    try:
        products_paginator= paginator.page(page)
    except PageNotAnInteger:
        products_paginator= paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    # context['categories']=ProductCategory.objects.all()
    context['categories'] = get_link_category()

    return render(request, 'mainapp/products.html', context)


class ProductDetailView(DetailView, BaseClassContentMixin):
    model = Product
    template_name = 'mainapp/product.html'
    title = 'geekshop - Подробное описание'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = get_product(self.kwargs.get('pk'))
        return context