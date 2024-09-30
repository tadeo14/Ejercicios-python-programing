"""
Crear una función que use lo visto de excepciones
para que tome por input() el número como str y
lo transforme directamente a float, sea entero o
decimal. Deberíamos pasar como argumento la
frase para mostrar en pantalla el pedido. Además,
deberíamos de volver a pedir, hasta que se pueda
hacer el ingreso de forma correcta.
A partir de ahora cada vez que tomemos un número
por teclado podemos hacer uso de esta función que
vamos a crear.

"""
def input_numerico(frase):
    dato = input(frase)
   
    while True: #hacemos un bucle mientras sea verdadero
        try:
            dato = int(dato)
            return dato
        except ValueError:
            try:
                dato = float(dato)
                return dato
            except ValueError:
                print("Error, no se pudo convertir a número")
        dato = input("Nuevamente.  " + frase)
    

    

#############################

edad = input_numerico("Ingrese su edad: ")
print(edad,type(edad))


if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

sube = input_numerico("Ingrese su saldo ")
print(sube,type(sube))

if sube < 0:
    print("No tienes saldo")
else:
    print("Su salo es", sube)

