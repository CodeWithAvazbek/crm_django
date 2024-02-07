from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')
