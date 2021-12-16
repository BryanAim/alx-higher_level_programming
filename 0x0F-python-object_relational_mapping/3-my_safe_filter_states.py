#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
