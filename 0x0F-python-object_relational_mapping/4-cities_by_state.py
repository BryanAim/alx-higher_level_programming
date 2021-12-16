#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
 a script that lists all cities from the database
"""
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                 JOIN states ON cities.state_id=states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
