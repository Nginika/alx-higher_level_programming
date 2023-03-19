#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host='localhost')

    cursor = db.cursor()
    check = sys.argv[4]
    cursor.execute("""SELECT * FROM states\
                    WHERE name LIKE '{}'\
                    ORDER BY states.id ASC;""".format(check.strip("'")))

    states = cursor.fetchall()
    for state in states:
        print(state)
