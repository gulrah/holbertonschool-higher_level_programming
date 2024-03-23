#!/usr/bin/python3
""" Module to filter states by user input """



import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM `states`")

    # Fetch all rows and filter by state name
    states = cursor.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
            
    # Close cursor and connection
    cursor.close()
    db.close()
