from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "link", "price")

admin.site.register(Book)
