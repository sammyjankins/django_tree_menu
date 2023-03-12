from django.contrib import admin
from .models import Category, Subcategory, CategoryItem

admin.site.register([Category, Subcategory, CategoryItem, ])
