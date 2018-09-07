# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from douban.models import BookType, Book

# Register your models here.
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(BookType, BookTypeAdmin)
admin.site.register(Book, BookAdmin)
