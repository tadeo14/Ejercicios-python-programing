import sqlite3

conn = sqlite3.connect("datos.sqlite3")

#armamos el cursor

cursor = conn.cursor() #esto lo hacemos para acortar las lineas de codigo

try:
    cursor.execute("CREATE TABLE personas (nombre TEXT, edad INT)")
    print("Bienvenido por primera vez")
except sqlite3.OperationalError:
    print("Bienvenido nuevamente")

cursor.execute("INSERT INTO personas VALUES (?,?)",("Roberto", 50))






conn.commit()
conn.close()