#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def main():
                """
    Connects to the MySQL database and retrieves the list of states sorted by their IDs.
    """
                    if len(sys.argv) != 4:
                                        print("Usage: {} username password database_name".format(sys.argv[0]))
                                                sys.exit(1)

                                                    username = sys.argv[1]
                                                        password = sys.argv[2]
                                                            database = sys.argv[3]

                                                                try:
                                                                                    db = MySQLdb.connect(
                                                                                                            host="localhost",
                                                                                                            port=3306,
                                                                                                            user=username,
                                                                                                            passwd=password,
                                                                                                            db=database,
                                                                                                            charset="utf8"
                                                                                                        )
                                                                                            cursor = db.cursor()
                                                                                                    cursor.execute("SELECT * FROM states ORDER BY id ASC")
                                                                                                            rows = cursor.fetchall()
                                                                                                                    for row in rows:
                                                                                                                                            print(row)
                                                                except MySQLdb.Error as e:
                                                                                    print("MySQL Error: {}".format(e))
                                                                                            sys.exit(1)
                                                                finally:
                                                                                    if db:
                                                                                                            db.close()


                                                                                                            if __name__ == "__main__":
                                                                                                                            main()
                                                                                                                            
