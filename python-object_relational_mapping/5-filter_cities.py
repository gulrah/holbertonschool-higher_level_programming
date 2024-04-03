#!/usr/bin/python3
"""Script that lists all cities of a given state from the database"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 5:
        try:
            db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
            )
            cursor = db.cursor()
            cursor.execute("""
                SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
            """, (sys.argv[4],))
            result = cursor.fetchone()
            if result[0]:
                print(result[0])
            else:
                print()
        except MySQLdb.Error as e:
            print("MySQL Error:", e)
        finally:
            if db:
                db.close()
    else:
        print("Usage: {} <username> <password> <database_name> <state_name>"
              .format(sys.argv[0]))
