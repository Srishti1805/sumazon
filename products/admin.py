# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture', 'price', 'description')
    search_fields = ('name',)
