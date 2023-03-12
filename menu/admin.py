from django.contrib import admin
from .models import MenuItem
from .forms import MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ['name', 'parent', 'url', 'root']
    list_filter = ['parent']


admin.site.register(MenuItem, MenuItemAdmin)
