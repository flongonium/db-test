import pymysql


con = pymysql.connect(host="192.168.178.33", user="sauna", password="1234", database="sauna")

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM sensor_values')

        rows = cur.fetchall()

        for row in rows:
            print("Temperatur beträgt aktuell: {}".format(row[2]))

finally:

    con.close()