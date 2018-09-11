# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from neteasy.models import MusicType, MusicList

# Register your models here.

class MusicTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

class MusicListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'my_url')
#
    # cusotmized field, let it be clickable
    def my_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)

    my_url.short_description = "播放列表"

admin.site.register(MusicType, MusicTypeAdmin)
admin.site.register(MusicList, MusicListAdmin)
