#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
a script that takes in the name of a state as an argument
and lists all cities of that state
"""
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 JOIN states ON cities.state_id=states.id\
                 WHERE states.name = %s", (argv[4],))
    rows = cur.fetchall()
    new_list = []
    for row in rows:
        new_list.append(row[0])
    print(", " .join(new_list))
    cur.close()
    db.close()
