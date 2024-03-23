#!/usr/bin/python3

"""
This script retrieves all states from the hbtn_0e_0_usa database and prints them.

Args:
    mysql_username: Username to connect to the MySQL server.
    mysql_password: Password to connect to the MySQL server.
    database_name: Name of the database to query.
"""

import MySQLdb


def main(mysql_username, mysql_password, database_name):
                        """
    Connects to the MySQL server, retrieves states, and prints them.
    """

                            try:
                                                        db = MySQLdb.connect(
                                                                                        host="localhost",
                                                                                        port=3306,
                                                                                        user=mysql_username,
                                                                                        passwd=mysql_password,
                                                                                        db=database_name,
                                                                                    )

                                                                cursor = db.cursor()

                                                                        # Retrieve states ordered by id
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
                                                                                                                            import sys

                                                                                                                                if len(sys.argv) != 4:
                                                                                                                                                            print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
                                                                                                                                                                    sys.exit(1)

                                                                                                                                                                        mysql_username, mysql_password, database_name = sys.argv[1:]
                                                                                                                                                                            main(mysql_username, mysql_password, database_name)
                                                                                                                                                                            
