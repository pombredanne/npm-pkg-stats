#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def insert(license, count):
    db = MySQLdb.connect("localhost","root","","registry")
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO LICENSE\
                VALUES ('%s', '%d')" %\
                (license, count))
        db.commit()
    except:
        db.rollback()
    db.close()
