
from django.urls import path
from mainapp.views import products, ProductDetailView, IndexTemplateView

app_name = 'products'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('products', products, name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('category/<int:id_category>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
]

