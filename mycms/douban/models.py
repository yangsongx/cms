# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookType(models.Model):
    type_name = models.CharField(max_length=100)


class Book(models.Model):
    book_type = models.ForeignKey(BookType)
    title = models.CharField(max_length=512)
    url = models.CharField(max_length=1024)
    rate = models.FloatField(null=True)
    pub = models.CharField(max_length=512)
    cover = models.CharField(max_length=1024, default='')
