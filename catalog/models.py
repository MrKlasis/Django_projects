from django import forms
from django.db import models
from django.utils.datetime_safe import date

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    img = models.ImageField(upload_to='category/', **NULLABLE, verbose_name='Изображение')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    author = models.ForeignKey('users.User', **NULLABLE, on_delete=models.SET_NULL, verbose_name='автор')
    name = models.CharField(max_length=100, verbose_name='Наименование', unique=True)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    img = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_begin = models.DateField(default=date.today, verbose_name='Дата создания')
    date_chang = models.DateField(default=date.today, verbose_name='Дата последнего изменения')
    publication = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('set_publication', 'Can publication'),
            # ('set_')
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=100, verbose_name='Наименование', unique=True)
    activate = models.BooleanField(default=False, verbose_name='Активировать')

    def __str__(self):
        return f'{self.name} ({self.number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
