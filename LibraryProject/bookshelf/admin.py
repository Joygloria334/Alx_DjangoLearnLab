from django.contrib import admin
from .models import Book

# Customize the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in list view
    list_filter = ('publication_year', 'author')             # Filters in sidebar
    search_fields = ('title', 'author')                      # Search box fields

# Register the model with the admin site
admin.site.register(Book, BookAdmin)
