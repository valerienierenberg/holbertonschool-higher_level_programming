#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM cities JOIN states ON cities.state_id =
               states.id WHERE states.name = %s ORDER BY cities.id ASC""",
                (argv[4],))
    query_rows = cur.fetchall()
    print_cities = []
    for row in query_rows:
        if row[4] == argv[4]:  # if state is a match to state argument passed
            print_cities.append(row[2])
            # ^ grabs city - ex. (8, 3, 'Dallas', 3, 'Texas')
    print(', '.join(print_cities))
    cur.close()
    conn.close()
