#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
a script that lists all states with a name starting with N (upper N)
"""
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY'N%'\
                ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
