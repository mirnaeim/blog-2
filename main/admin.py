from django.contrib.admin import register
from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.


@register(Category,)
class CategoryAdmin(admin.ModelAdmin):
    pass


@register(Post,)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'category')
    prepopulated_fields = {"slug": ("title",)}


@register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'post')
