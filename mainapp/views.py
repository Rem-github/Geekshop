from django.shortcuts import render, get_object_or_404


# Create your views here.
from mainapp.models import Products


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    product = Products.objects.all()
    context = {
        'title': 'geekshop - Каталог',
        'product': product
        #'products': [
        #    {'name': 'Худи черного цвета с монограммами adidas Originals', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'photo': '/static/vendor/img/products/Adidas-hoodie.png', 'price': 6090},
        #    {'name': 'Синяя куртка The North Face', 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'photo': '/static/vendor/img/products/Blue-jacket-The-north-Face.png', 'price': 23725},
        #    {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'photo': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'price': 3390},
        #    {'name': 'Черный рюкзак Nike Heritage', 'description': 'Плотная ткань. Легкий материал.', 'photo': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png', 'price': 2340},
        #    {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'description': 'Гладкий кожаный верх. Натуральный материал.', 'photo': '/static/vendor/img/products/Black-Dr-Martens-shoes.png', 'price': 13590},
        #    {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'photo': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'price': 2890},
        #]

    }
    return render(request, 'mainapp/products.html', context)

