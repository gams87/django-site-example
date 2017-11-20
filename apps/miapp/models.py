# -*- encoding: utf-8 -*-
from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(verbose_name='Activo', default=True)
    create_date = models.DateTimeField(verbose_name='Fecha creación', editable=False, auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(verbose_name='Nombre', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id']


class Product(BaseModel):
    TYPE_OF_PURCHASE = (
        ('Diario', 'Diario'),
        ('Semanal', 'Semanal'),
        ('Quincenal', 'Quincenal'),
        ('Mensual', 'Mensual'),
        ('Bimensual', 'Bimensual'),
        ('Trimestral', 'Trimestral'),
        ('Semestral', 'Semestral'),
        ('Anual', 'Anual'),
    )

    name = models.CharField(verbose_name='Descripción', max_length=100, unique=True)
    price = models.DecimalField(verbose_name='Precio', max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name='Categoría')
    type_of_purchase = models.CharField(verbose_name='Tipo de compra', max_length=30, choices=TYPE_OF_PURCHASE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Producto'
        ordering = ['-id']


    def iva(self):
        return int(self.price) * 1.13