#!/usr/bin/python3
"""
lists all cities of the database hbtn_0e_4_usa, ordered by city id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states\
             WHERE cities.state_id = states.id"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
