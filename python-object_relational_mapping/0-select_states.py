#!/usr/bin/python3
"""
Lists all states from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
                    # Check if correct number of arguments provided
                    if len(sys.argv) != 4:
                                            print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
                                                    sys.exit(1)

                                                        # Establish connection to MySQL database
                                                            try:
                                                                                    db = MySQLdb.connect(
                                                                                                                host="localhost",
                                                                                                                port=3306,
                                                                                                                user=sys.argv[1],
                                                                                                                passwd=sys.argv[2],
                                                                                                                db=sys.argv[3]
                                                                                                            )
                                                            except MySQLdb.Error as e:
                                                                                    print("Error {}: {}".format(e.args[0], e.args[1]))
                                                                                            sys.exit(1)

                                                                                                # Create cursor object
                                                                                                    cursor = db.cursor()

                                                                                                        # Execute SQL query
                                                                                                            try:
                                                                                                                                    cursor.execute("SELECT * FROM states ORDER BY id ASC")
                                                                                                            except MySQLdb.Error as e:
                                                                                                                                    print("Error {}: {}".format(e.args[0], e.args[1]))
                                                                                                                                            cursor.close()
                                                                                                                                                    db.close()
                                                                                                                                                            sys.exit(1)

                                                                                                                                                                # Fetch and print results
                                                                                                                                                                    for row in cursor.fetchall():
                                                                                                                                                                                            print(row)

                                                                                                                                                                                                # Close cursor and database connection
                                                                                                                                                                                                    cursor.close()
                                                                                                                                                                                                        db.close()
                                                                                                                                                                                                        
