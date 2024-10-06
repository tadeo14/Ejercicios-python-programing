import pymysql
from tabulate import tabulate


conn = conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    db="alumnos"
)

#armamos el cursor

cursor = conn.cursor() #esto lo hacemos para acortar las lineas de codigo

t = (("Osvaldo", 38),("Tamara",48), ("Amalia",55))

for nombre, edad in t:
    cursor.execute("INSERT INTO personas VALUES(%s,%s)", (nombre, edad ))

cursor.execute("SELECT * FROM personas")

data = cursor.fetchall()


conn.commit()
conn.close()

print(data)
