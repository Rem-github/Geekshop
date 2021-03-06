from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from baskets.models import Basket
from mainapp.mixin import BaseClassContentMixin
from mainapp.models import Product
from ordersapp.forms import OrderForm, OrderItemsForm
from ordersapp.models import Order, OrderItem


class OrderList(ListView, BaseClassContentMixin):
    model = Order
    title = 'GeekShop | Список заказов'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(ListView, self).dispatch(*args, **kwargs)

class OrderCreate(CreateView, BaseClassContentMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'GeekShop | Создание заказа'

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(OrderCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_item = Basket.objects.filter(user=self.request.user)
            if basket_item:
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=basket_item.count())
                formset = OrderFormSet()
                for num,form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[num].product
                    form.initial['quantity'] = basket_item[num].quantity
                    form.initial['price'] = basket_item[num].product.price
                basket_item.delete()
            else:
                formset = OrderFormSet()
        context['orderitems']= formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrderCreate, self).form_valid(form)



class OrderUpdate(UpdateView, BaseClassContentMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'GeekShop | Обновление заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price


        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrderUpdate, self).form_valid(form)

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(OrderUpdate, self).dispatch(*args, **kwargs)

class OrderDelete(DeleteView, BaseClassContentMixin):
    model = Order
    success_url = reverse_lazy('orders:list')
    title = 'GeekShop | Удаление заказа'


class OrderDetail(DetailView, BaseClassContentMixin):
    model = Order
    title = 'GeekShop | Просмотр заказа'

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(OrderDetail, self).dispatch(*args, **kwargs)


# class HttpResponseRedirect:
#     pass


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('orders:list'))

def get_product_price(request,pk):
    if request.is_ajax():
        product=Product.objects.get(pk=pk)
        if product:
            return JsonResponse({'price':product.price})
        return JsonResponse({'price':0})

