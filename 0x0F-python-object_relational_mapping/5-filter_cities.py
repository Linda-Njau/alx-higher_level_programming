#!/usr/bin/python3
"""displays all cities in a specified state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor() 
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states on cities.state_id = state.id WHERE state.name LIKE %s \
    ORDER BY cities.id", (argv[4]))
    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))
    cursor.close()
    db.close()