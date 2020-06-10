from django.contrib import admin

# Register your models here.

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'avilable', 'created', 'updated']
    list_filter = ['avilable', 'created', 'updated']
    list_editable = ['price', 'stock', 'avilable']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product,ProductAdmin)

