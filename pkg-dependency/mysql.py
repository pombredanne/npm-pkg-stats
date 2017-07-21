#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def increase(pkg, isDev=True):
    db = MySQLdb.connect("localhost","root","","registry")
    cursor = db.cursor()
    field = 'dev' if isDev else 'dependency'
    dependency = 0 if isDev else 1
    dev = 1 if isDev else 0
    try:
        cursor.execute("INSERT INTO dependency VALUES ('%s', '%d', '%d', 1)\
            ON DUPLICATE KEY UPDATE total=total+1, %s=%s+1;" %(pkg, dependency, dev, field, field))
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()
