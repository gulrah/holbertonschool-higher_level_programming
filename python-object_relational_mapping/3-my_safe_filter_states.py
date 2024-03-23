"""Safely queries the database for state names."""
import sys
import MySQLdb

if __name__ == "__main__":
        # Check for correct number of arguments
        if len(sys.argv) != 5:
                    print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username, password, database_name, state_name = sys.argv[1:]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database_name, charset="utf8")
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    # Create cursor object
    cursor = db.cursor()

    # Execute safe query using parameters
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    try:
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        cursor.close()
        db.close()
        sys.exit(1)

    # Close cursor and database connection
    cursor.close()
    db.close()
