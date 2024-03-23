#!/usr/bin/python3

"""
This script retrieves all states from the specified database and prints them.
"""

import MySQLdb
import sys


def main():
                            """
    Main function to connect to the database, retrieve states, and print them.
    """

                                if len(sys.argv) != 4:
                                                                print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
                                                                        sys.exit(1)

                                                                            mysql_username = sys.argv[1]
                                                                                mysql_password = sys.argv[2]
                                                                                    database_name = sys.argv[3]

                                                                                        try:
                                                                                                                        db = MySQLdb.connect(
                                                                                                                                                            host="localhost",
                                                                                                                                                            port=3306,
                                                                                                                                                            user=mysql_username,
                                                                                                                                                            passwd=mysql_password,
                                                                                                                                                            db=database_name,
                                                                                                                                                        )

                                                                                                                                cursor = db.cursor()

                                                                                                                                        cursor.execute("SELECT * FROM states ORDER BY id ASC")
                                                                                                                                                states = cursor.fetchall()

                                                                                                                                                        for state in states:
                                                                                                                                                                                            print(state)

                                                                                        except MySQLdb.Error as err:
                                                                                                                        print(f"Error: {err}")

                                                                                        finally:
                                                                                                                        if db:
                                                                                                                                                            cursor.close()
                                                                                                                                                                        db.close()


                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                    main()
                                                                                                                                                                                                    
