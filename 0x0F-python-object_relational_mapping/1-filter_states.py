#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name like 'N%' ORDER BY
                states.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
