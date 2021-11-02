from rest_framework import serializers
from .models import Product, Profile, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ('pk', 'name', 'photo', 'description', 'price')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = ('pk', 'user', 'image', 'bio')


class ReviewSerializier(serializers.ModelSerializer):
    class Meta:
        model = Review

        fields = ('pk', 'user', 'product', 'rating', 'body')
