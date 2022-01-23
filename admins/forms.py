from django import forms
from django.forms import ModelForm

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class AdminProductCategory(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())

class CategoryAdminCreateForm(ModelForm):
    description = forms.CharField(widget=forms.TextInput())
    discount = forms.IntegerField(widget=forms.NumberInput(), label='скидка', required=False, min_value=0, max_value=90)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'discount')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class ProductAdminCreateForm(ModelForm):
    description = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Product
        fields = ('name', 'description','photo', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductAdminCreateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['photo'].widget.attrs['class'] = 'custom-file-input'