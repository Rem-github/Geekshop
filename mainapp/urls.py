
from django.urls import path
from mainapp.views import products, product

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('product/<int:id>/', product, name='product'),

]

