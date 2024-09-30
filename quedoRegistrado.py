"""
Hacer un pequeño programa con un menú
muy sencillo:
Menú:
1 – Ingreso de empleado
2 – Egreso de empleado
3 – Salir del sistema
>>>
Este sistema es básico, lo utiliza el personal
de seguridad que registra el nombre de la
persona que ingresa (opción 1), y que egresa
del edificio (opción 2).
Además, es necesario registrar el horario de
los eventos se podría usar el módulo time, y
la función asctime() que devuelve un str
con fecha y hora.
Cuando se quiere salir del programa se usa la
opción 3.
Tanto el ingreso y el egreso se registra en un
archivo txt. Cada renglón representa un
registro.
"""

import time 

#######################
#AREA DE FUNCIONES 

#creamos una funcion llamada guardar 
def guardar(fech,nom,eve):
    
    f = open("registro.txt","a")
    f.write(f"{fech}--{nom}--{eve}\n")
    f.close()
    print("evento salvado")




###########################3

while True:
    print("1- Ingreso")
    print("2- Egreso")
    print("3- Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del empleado: ")
        evento = "ingreso"
        fecha = time.asctime()
        guardar(fecha,nombre,evento)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        evento = "ingreso"
        fecha = time.asctime()
        guardar(fecha,nombre,evento)
    elif opcion == "3":
        print("adiós")
        break
    else:
        print("Opción no válida")
