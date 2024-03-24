#!/usr/bin/python3
# Lists specific cities from the database hbtn_0e_4_usa.
# Usage: ./4-cities_by_state.py <mysql username> \
    #                               <mysql password> \
    #                               <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
        FROM `cities` as `c` \
        INNER JOIN `states` as `s` \
        ON `c`.`state_id` = `s`.`id` \
        WHERE `c`.`name` IN ('San Francisco', 'San Jose', 'Los Angeles', 'Fremont', 'Livermore', \
        'Page', 'Phoenix', 'Dallas', 'Houston', 'Austin', 'New York', \
        'Las Vegas', 'Reno', 'Henderson', 'Carson City') \
        ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
