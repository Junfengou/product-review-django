from django.contrib import admin
from .models import Product, Profile, Review

# Register your models here.


class ProductList(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']
    ordering = ['name']


class ReviewList(admin.ModelAdmin):
    list_display = ('product', 'rating')
    list_filter = ('product', 'rating')
    search_fields = ('product', 'rating')
    ordering = ['product']


class ProfileList(admin.ModelAdmin):
    list_display = ('user', 'image', 'bio')
    list_filter = ('user', 'image', 'bio')
    search_fields = ('user', 'image', 'bio')
    ordering = ['user']


admin.site.register(Product, ProductList)
admin.site.register(Review, ReviewList)
admin.site.register(Profile, ProfileList)