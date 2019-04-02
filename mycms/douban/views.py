# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json
from douban.models import Book, BookType
# Create your views here.

def foo(request):
    ret = {
     'name':'hello'
    }
    book = Book.objects.filter(book_type__type_name = 'mytype')
    print("There are totally %d book found" %(len(book)))
    for it in book:
        print("Title - %s, Cover - %s, Type - %s" %(it.title, it.cover, it.book_type.type_name))

    print("\n==second method==")
    bt = BookType.objects.get(type_name = 'mytype')
    book2 = Book.objects.filter(book_type = bt)
    print("[2nd]There are totally %d book found" %(len(book2)))
    for it in book2:
        print("Title - %s, Cover - %s, Type - %s" %(it.title, it.cover, it.book_type.type_name))

    return HttpResponse(json.dumps(ret), content_type="application/json")
