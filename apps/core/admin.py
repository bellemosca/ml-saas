from django.contrib import admin

from .models import ModelML

# Register your models here.


@admin.register(ModelML)
class ModelMLAdmin(admin.ModelAdmin):
    pass
