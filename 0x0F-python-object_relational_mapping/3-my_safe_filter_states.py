#!/usr/bin/python3
"""
displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT * FROM states\
             WHERE states.name = %s\
             ORDER BY states.id ASC"
    cursor = db.cursor()
    cursor.execute(query, (argv[4], ))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
