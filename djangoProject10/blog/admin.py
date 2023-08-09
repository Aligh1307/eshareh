from django.contrib import admin
from .models import Word, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'picture', 'parent')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('slug', 'title')


admin.site.register(Category, CategoryAdmin)


class WordAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'video', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Word, WordAdmin)
