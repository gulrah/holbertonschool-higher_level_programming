#!/usr/bin/python3
""" Module to list all states """

if __name__ == "__main__":
                    import MySQLdb
                        from sys import argv

                            try:
                                                    # Connecting to MySQL server using command-line arguments
                                                    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

                                                            # Creating cursor object
                                                                    cursor = db.cursor()

                                                                            # Executing SQL query
                                                                                    cursor.execute("SELECT * FROM states ORDER BY id ASC")

                                                                                            # Fetching all rows from the result set
                                                                                                    rows = cursor.fetchall()

                                                                                                            # Printing results
                                                                                                                    for row in rows:
                                                                                                                                                print(row)

                            except MySQLdb.Error as e:
                                                    print("An error occurred:", e)
                            finally:
                                                    # Closing cursor and database connection
                                                    cursor.close()
                                                            db.close()
                                                            
