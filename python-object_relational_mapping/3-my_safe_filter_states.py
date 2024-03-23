#!/usr/bin/python3
""" Module to list all states """


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` WHERE `name` = %s", (sys.argv[4],))
    [print(state) for state in cursor.fetchall()]
