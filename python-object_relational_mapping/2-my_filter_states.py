#!/usr/bin/python3
""" takes in an argument and displays all values
in the states tablee of hbtn_0e_0_usa where name matches the argument """

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
    WHERE name LIKE BINARY '{}' \
    ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
    