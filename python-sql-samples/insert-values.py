import pymysql


connection = pymysql.Connect(host="192.168.178.33", user="sauna", password="1234", database="sauna")

connection.begin()
cursor = connection.cursor()

query = 'INSERT INTO `sensor_values` (`temp`, `hum`) VALUES (%s, %s)'
insert_values = ("28", "60")
connection.cursor().execute(query, insert_values[:])
connection.commit()
cursor.close()
connection.close()