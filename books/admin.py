from django.contrib import admin

from books.models import Book

class BookAdmin(admin.ModelAdmin):
    fields = (('author', 'title'), 'book_pic', ('date_reading', 'favorite'), 'action', 'review')

admin.site.register(Book, BookAdmin)