from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='product_image', verbose_name='Фото')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.name} | {self.category}'

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
