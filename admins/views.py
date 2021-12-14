from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, AdminProductCategory, CategoryAdminCreateForm, \
    CategoryAdminCreateForm, ProductAdminCreateForm
from authapp.models import User
from mainapp.mixin import BaseClassContentMixin, CustomDispatchMixin
from mainapp.models import ProductCategory, Product

class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'

# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'admins/admin.html')


class UserListView(ListView, BaseClassContentMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = "Geekshop Админ | Список пользователей"


class UserCreateView(CreateView, BaseClassContentMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = "Geekshop Админ | Регистрация"


class UserUpdateView(UpdateView, BaseClassContentMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = "Geekshop Админ | Обновление"


class UserDeleteView(DeleteView, BaseClassContentMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductCategoryListView(ListView, BaseClassContentMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = "Geekshop Админ | Список категорий"



class ProductCategoryCreateView(CreateView, BaseClassContentMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryAdminCreateForm
    success_url = reverse_lazy('admins:admin_category')
    title = "Geekshop Админ | Добавление категорий"


class ProductCategoryUpdateView(UpdateView, BaseClassContentMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/category-users-update-delete.html'
    form_class = CategoryAdminCreateForm
    success_url = reverse_lazy('admins:admin_category')
    title = "Geekshop Админ | Обновление"


class ProductCategoryDeleteView(DeleteView, BaseClassContentMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-users-update-delete.html'
    form_class = CategoryAdminCreateForm
    success_url = reverse_lazy('admins:admin_category')


class ProductListView(ListView, BaseClassContentMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = "Geekshop Админ | Список товаров"



class ProductCreateView(CreateView, BaseClassContentMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')
    title = "Geekshop Админ | Добавление продуктов"



class ProductUpdateView(UpdateView, BaseClassContentMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')
    title = "Geekshop Админ | Обновление"


class ProductDeleteView(DeleteView, BaseClassContentMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')