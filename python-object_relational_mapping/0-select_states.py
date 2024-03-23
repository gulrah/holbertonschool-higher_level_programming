#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
                                # Establish connection to MySQL database
                                db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
                                    cursor = db.cursor()

                                        # Execute SQL query
                                            cursor.execute("SELECT * FROM `states`")

                                                # Fetch and print results
                                                    for state in cursor.fetchall():
                                                                                        print(state)
