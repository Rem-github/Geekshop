from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from admins.forms import UserAdminProfileForm
from authapp.forms import UserProfileForm
from baskets.models import Basket
from mainapp.mixin import BaseClassContentMixin, CustomDispatchMixin
from mainapp.models import Product


# @login_required
# def basket_add(request, id):
#     user_select = request.user
#     product = Product.objects.get(id=id)
#     baskets = Basket.objects.filter(user=user_select, product=product)
#
#     if baskets:
#         basket = baskets.first()
#         basket.quantity += 1
#         basket.save()
#     else:
#         Basket.objects.create(user=user_select, product=product, quantity=1)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # возврат на страницу где была нажата кнопка

@login_required
def basket_add(request, id):
    if request.is_ajax():
        user_select = request.user
        product = Product.objects.get(id=id)
        baskets = Basket.objects.filter(user=user_select, product=product)

    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=user_select, product=product, quantity=1)

    products = Product.objects.all()
    context = {
        'products': products, # ключ такой же как в card.html,
    }
    result = render_to_string('mainapp/includes/card.html', context)
    return JsonResponse({'result': result})


# class BasketDeleteView(DeleteView):
#     model = Basket
#     template_name = ''
#     form_class = UserProfileForm
#     success_url = reverse_lazy('authapp:profile')


@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, basket_id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=basket_id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

    baskets = Basket.objects.filter(user=request.user)
    context = {
        'baskets': baskets  # ключ такой же как в basket.html
    }
    result = render_to_string('baskets/basket.html', context)
    return JsonResponse({'result': result})
