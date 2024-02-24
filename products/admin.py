# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Products, Order


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'picture',
        'price',
        'description',
        'quantity',
    )
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'incomingData')
    list_filter = ('userId',)
