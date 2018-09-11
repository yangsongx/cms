# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#
class MusicType(models.Model):
    type_name = models.CharField(max_length=100)
    def __str__(self):
        return self.type_name

class MusicList(models.Model):
    list_type = models.ForeignKey(MusicType)
    title = models.CharField(max_length=512)
    url = models.CharField(max_length=1024)
    cover = models.CharField(max_length=1024, default='')
    played = models.CharField(max_length=32, default='')

    class Meta:
        verbose_name = '音乐列表'
        verbose_name_plural = '音乐列表'

    def __str__(self):
        return self.title
