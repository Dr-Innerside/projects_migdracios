from django.contrib import admin
from .models import Category, Drink

# Register your models here.
admin.site.register(Drink)
admin.site.register(Category)