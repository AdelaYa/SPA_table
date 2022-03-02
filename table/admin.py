from django.contrib import admin

from . import models


@admin.register(models.Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'count', 'distance')
    ordering = ('name', 'count', 'distance')
