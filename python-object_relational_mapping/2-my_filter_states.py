#!/usr/bin/python3
""" Module to filter states by user input """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
    # Connecting to MySQL server using command-line arguments
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
        
        # Creating cursor object
        cursor = db.cursor()

        # Constructing SQL query with user input
        query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
        state_name = (argv[4],)  # Note: comma is necessary for single element tuple
        cursor.execute(query, state_name)
        
        # Fetching all rows from the result set
        rows = cursor.fetchall()
        
        # Printing results
        for row in rows:
            print(row)
            
    except MySQLdb.Error as e:
        print("An error occurred:", e)
    finally:
        # Closing cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

