import pymysql

# Open database connection
db = pymysql.connect("192.168.178.33","sauna","1234","sauna" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM sensor_values")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
for dat in data:
    print(dat)

# disconnect from server
db.close()