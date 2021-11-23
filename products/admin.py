from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# Managing products and offers in the admin area
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
