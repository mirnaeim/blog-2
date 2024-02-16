from django.contrib.admin import register
from django.contrib import admin
from .models import Category, Post
# Register your models here.


@register(Category,)
class CategoryAdmin(admin.ModelAdmin):
    pass


@register(Post,)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}