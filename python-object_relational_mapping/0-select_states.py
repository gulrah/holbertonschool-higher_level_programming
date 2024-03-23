#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
        # Get command line arguments
        mysql_username = sys.argv[1]
            mysql_password = sys.argv[2]
                database_name = sys.argv[3]

                    # Connect to MySQL server
                        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                                                                      passwd=mysql_password, db=database_name)

                            # Create a cursor object
                                cursor = db.cursor()

                                    # Execute the query
                                        cursor.execute("SELECT * FROM states ORDER BY id ASC")

                                            # Fetch all the rows
                                                rows = cursor.fetchall()

                                                    # Display the results
                                                        for row in rows:
                                                                    print(row)

                                                                        # Close cursor and database connection
                                                                            cursor.close()
                                                                                db.close()
                                                                                
