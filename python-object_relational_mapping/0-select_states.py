""" Module to list all states """

import MySQLdb
import sys

def connect_and_print_states(mysql_username, mysql_password, database_name):
    """
    Connects to the database, retrieves states, and prints them.
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

# Only execute the code if the script is run directly
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Call the function with arguments from command line
    connect_and_print_states(sys.argv[1], sys.argv[2], sys.argv[3])
