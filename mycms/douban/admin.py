# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from douban.models import BookType, Book
from django.utils.html import format_html

# Register your models here.
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'my_url')
    search_fields = ('title',)

    # cusotmized field, let it be clickable
    def my_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)

    my_url.short_description = "书籍详情"

admin.site.register(BookType, BookTypeAdmin)
admin.site.register(Book, BookAdmin)
