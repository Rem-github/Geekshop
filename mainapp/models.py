from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(verbose_name='Фото')
    price = models.IntegerField(verbose_name='Цена')

