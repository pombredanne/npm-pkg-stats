#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb


def increase(keyword):
    db = MySQLdb.connect("localhost", "root", "", "newregistry")
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO keywords VALUES ('%s', 1)\
            ON DUPLICATE KEY UPDATE count=count+1;" % (keyword))
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()
