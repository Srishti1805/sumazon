# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'address',
        'email',
        'password',
        'number',
        'profilePicture',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    raw_id_fields = ('groups', 'user_permissions')
