from django.contrib import admin

from .models import Product, Job, Image

class ProductAdmin(admin.ModelAdmin):
    exclude=("users",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Job)
admin.site.register(Image)

