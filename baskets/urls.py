
from django.urls import path
from baskets.views import *

app_name = 'baskets'

urlpatterns = [
    path('add/<int:id>/', basket_add, name='basket_add'),
    path('remove/<int:pk>/', basket_remove, name='basket_remove'),
    path('edit/<int:basket_id>/<int:quantity>/', basket_edit, name='basket_edit'),
]

