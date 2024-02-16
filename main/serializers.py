from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'body',
            'created_date',
            'updated_date',
        )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'slug',
            'category',
            'created_date',
            'updated_date',
        )
