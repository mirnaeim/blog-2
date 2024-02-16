from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('pk')


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('pk')
