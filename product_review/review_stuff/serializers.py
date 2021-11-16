from rest_framework import serializers
from .models import Product, Profile, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


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
