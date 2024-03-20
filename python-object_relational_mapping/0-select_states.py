#!/usr/bin/python3
""" Module to list all states """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)
        
    # Connecting to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    except MySQLdb.Error as e:
        print("Error: Unable to connect to MySQL database:", e)
        exit(1)
        
    # Creating cursor object
    cursor = db.cursor()

    # Executing SQL query
    try:
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    except MySQLdb.Error as e:
        print("Error: Unable to execute SQL query:", e)
        cursor.close()
        db.close()
        exit(1)
        
    # Fetching all rows from the result set
    rows = cursor.fetchall()
    
    # Printing results
    for row in rows:
        print(row)
        
    # Closing cursor and database connection
    cursor.close()
    db.close()
