# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import re
import sqlite3
import sys

class ImportData:
    __jsfn = ''
    __dbconn = None
    __dbcur = None
    __book_table = 'douban_book'

    def __init__(self, fn):
        self.__jsfn = fn
        self.__dbconn = sqlite3.connect("./db.sqlite3")
        self.__dbcur = self.__dbconn.cursor()

    def convert_quote(self, data):
        ret = ''

        for i in data:
            if i == "\"" or i == "'":
                print("Wow, you need add quote")
                ret = ret + "\\"
                ret = ret + i
            else:
                ret = ret + i

        return ret
    def load_in(self, jsobj):

        typeid = 1 # programming by default
        if jsobj['tag'] == 0:
            typeid = 1

        cmd = "INSERT INTO %s (title, url, rate, book_type_id, cover, pub) VALUES ('%s', '%s', %f, %d, '%s', 'TODO');" \
               %(self.__book_table,
                 self.convert_quote(jsobj['title']) , jsobj['url'], jsobj['rating'] , typeid, jsobj['cover'])
#        cmd = "INSERT INTO {} (title, url, rate, book_type_id, cover, pub) VALUES ({}, {}, {}, {}, {}, {});".format(\
#               self.__book_table,
#                 jsobj['title'] , jsobj['url'], jsobj['rating'] , typeid, jsobj['cover'], jsobj['author'])
        print("the SQL cmd:%s" %(cmd))
#        self.__dbcur.execute("INSERT INTO ? (title, url, rate, book_type_id, cover, pub) VALUES (?, ?, ?, ?, ?)",\
#                (self.__book_table,
#                 jsobj['title'] , jsobj['url'], jsobj['rating'] , typeid, jsobj['cover']))
        self.__dbcur.execute(cmd)
        self.__dbconn.commit()

        return 0

    def run(self):
        with open(self.__jsfn, 'r') as f:
            full_data = f.read()
            jsdata = json.loads(full_data)
            print("json loaded[OK]")
            print("there are totally %d items" %(len(jsdata)))

            cmd = "DELETE FROM %s;" %(self.__book_table)
            self.__dbcur.execute(cmd)
            self.__dbconn.commit()

            for it in jsdata:
                self.load_in(it)

        return 0

if __name__ == '__main__':
    jsfile = sys.argv[1]
    print("try import the data from %s" %(jsfile))

    im = ImportData(jsfile)
    im.run()
