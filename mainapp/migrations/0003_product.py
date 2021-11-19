# Generated by Django 3.2.9 on 2021-11-19 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='product_image', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory')),
            ],
        ),
    ]
