#!/usr/bin/python3
# Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
# Usage: ./4-cities_by_state.py <mysql username> \
    #                               <mysql password> \
    #                               <database name>
import sys
import MySQLdb

def insert_states(cursor):
    states = ["California", "Arizona", "Texas", "New York", "Nevada"]
    for state in states:
        cursor.execute("SELECT id FROM states WHERE name = %s", (state,))
        result = cursor.fetchone()
        if not result:
            cursor.execute("INSERT INTO states (name) VALUES (%s)", (state,))
            
if __name__ == "__main__":
    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        
        # Insert states if they don't already exist
        insert_states(c)

        c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                    FROM `cities` as `c` \
                    INNER JOIN `states` as `s` \
                       ON `c`.`state_id` = `s`.`id` \
                    ORDER BY `c`.`id`")
        [print(city) for city in c.fetchall()]
        
        c.close()
        db.close()
    except Exception as e:
            print("Error:", e)
