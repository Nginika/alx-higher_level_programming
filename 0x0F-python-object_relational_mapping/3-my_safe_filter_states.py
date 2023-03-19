#!/usr/bin/python3
"""
takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
    cursor.execute('SELECT * FROM states\
                    WHERE name = %s\
                    ORDER BY states.id ASC', (sys.argv[4], ))

    states = cursor.fetchall()
    for state in states:
        print(state)
