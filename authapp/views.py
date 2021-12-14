from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from baskets.models import Basket

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = auth.authenticate(username=username, password=password)
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'title': 'Geekshop | Авторизация',
#         'form': form,
#     }
#     return render(request, 'authapp/login.html', context)
from mainapp.mixin import BaseClassContentMixin, UserDispatchMixin, CustomDispatchMixin


class UserLoginView(LoginView, BaseClassContentMixin):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    title = "Geekshop | Авторизация"


# def register(request):
#
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Вы успешно зарегистрировались!")
#             return HttpResponseRedirect(reverse('authapp:login'))
#     else:
#         form = UserRegisterForm()
#     context = {
#         'title': 'Geekshop | Регистрация',
#         'form': form,
#     }
#     return render(request, 'authapp/register.html', context)

class UserCreateView(CreateView):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('authapp:login')
    title = "Geekshop | Регистрация"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.success(request, "Вы успешно зарегистрировались!")
            else:
                messages.error(request, "Проверьте правильность ввода")
        else:
            messages.error(request, "Проверьте правильность ввода")
        return render(request, self.template_name, {'form': form})

    # def send_verify_link(self, user):
    #
    #     verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
    #     subject = f'Для активации учетной записи {user.username} пройдите по ссылке'
    #     message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
    #     return send_mail(subject, message, settings.EMAIL_HOST_USER)
    #
    # def verify(self):
    #     pass


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Данные успешно обновлены!")
#         else:
#             messages.error(request, "Проверьте правильность ввода")
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {
#         'title': 'Geekshop | Профайл',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user)
#     }
#     return render(request, 'authapp/profile.html', context)

class ProfileFormView(UpdateView, BaseClassContentMixin, UserDispatchMixin):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    title = "Geekshop | Профайл"

    def form_valid(self, form):
        messages.success(self.request, 'Данные успешно изменены')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')

class UserLogoutView(LogoutView, BaseClassContentMixin):
    template_name = 'mainapp/index.html'
