from django.contrib import admin
from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('title', 'category', 'status', 'featured', 'created_at')
    list_filter    = ('status', 'category', 'featured')
    search_fields  = ('title', 'excerpt', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_editable  = ('status', 'featured')
    date_hierarchy = 'created_at'
    ordering       = ('-created_at',)
