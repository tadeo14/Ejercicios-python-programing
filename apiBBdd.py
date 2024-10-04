import sqlite3
from tabulate import tabulate


conn = sqlite3.connect("datos.sqlite3")

#armamos el cursor

cursor = conn.cursor() #esto lo hacemos para acortar las lineas de codigo

try:
    cursor.execute("CREATE TABLE personas (nombre TEXT, edad INT)")
    print("Bienvenido por primera vez")
except sqlite3.OperationalError:
    print("Bienvenido nuevamente")


# t = (("Osvaldo",30),("Juan", 40), ("hector",62))

# for nombre,edad in t:
#     cursor.execute("INSERT INTO personas VALUES (?,?)",(nombre, edad))


#seleccionamos toda la tabla
cursor.execute("SELECT * FROM personas")

#guardamos los datos en una variable
data = cursor.fetchall()

conn.commit()
conn.close()

#sera una lista de tuplas


print(tabulate(data,["Nombre", "Edad"],tablefmt="pretty"))