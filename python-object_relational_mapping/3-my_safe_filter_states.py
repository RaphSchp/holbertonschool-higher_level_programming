#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states
where name matches the argument.
But this time, write one that is safe from MySQL injections"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = database.cursor()
    query = "SELECT * FROM states \
    WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name, ))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
    