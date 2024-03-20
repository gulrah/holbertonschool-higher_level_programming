#!/usr/bin/python3
""" Module to list all states """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connecting to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Creating cursor object
    cursor = db.cursor()

    # Executing SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Printing results
    for row in rows:
        print(row)
        
    # Closing cursor and database connection
    cursor.close()
    db.close()
