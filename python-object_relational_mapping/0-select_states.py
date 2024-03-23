#!/usr/bin/python3
"""Lists all states from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
                # Establish connection to MySQL database
                db = MySQLdb.connect(
                                    host="localhost",
                                    port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3]
                                )

                    # Create cursor object
                        cursor = db.cursor()

                            # Execute SQL query
                                cursor.execute("SELECT * FROM states ORDER BY id ASC")

                                    # Fetch and print results
                                        for row in cursor.fetchall():
                                                            print(row)

                                                                # Close cursor and database connection
                                                                    cursor.close()
                                                                        db.close()
                                                                        
