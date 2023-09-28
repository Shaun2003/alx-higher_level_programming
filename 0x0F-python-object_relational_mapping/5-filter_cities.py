#!/usr/bin/python3
"""
Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
Safe from SQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT cities.name\
             FROM cities JOIN states\
             ON cities.state_id = states.id\
             WHERE states.name = %s"
    cursor = db.cursor()
    cursor.execute(query, (argv[4], ))
    cities = []
    for city in cursor.fetchall():
        cities.append(city[0])
    print(", ".join(cities))
    cursor.close()
    db.close()
