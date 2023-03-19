#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
    cursor.execute(
            'SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON\
            cities.state_id = states.id;')

    states = cursor.fetchall()

    for state in states:
        print(state)
