
from django.urls import path
from baskets.views import *

app_name = 'baskets'

urlpatterns = [
    path('add/<int:id>/', basket_add, name='basket_add'),
    path('remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
