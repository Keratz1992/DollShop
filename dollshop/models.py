from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название')


    def __str__(self):
        return f'{self.name}'



class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')


    def __str__(self):
        return f'{self.category}, {self.name}, {self.price}, {self.date_create}'
