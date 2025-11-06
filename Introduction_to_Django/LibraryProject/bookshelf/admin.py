from django.contrib import admin
from .models import Book

# Register the Book model with custom admin options
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Shows columns in admin list view
    search_fields = ('title', 'author')                     # Enables search by title and author
    list_filter = ('publication_year',)                     # Enables filtering by publication year
