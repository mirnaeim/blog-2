from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Post, Comment


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):
    #author = UserSerializer()

    class Meta:
        model = Comment
        fields = (
            'body',
            'author',
            'post',
        )


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    comments = CommentSerializer(many=True)

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
            'comments',
        )
