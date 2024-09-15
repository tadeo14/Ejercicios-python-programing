"""
Ejercicio 1: Países
Crear un script que solicite al usuario el
código de un país e imprima su nombre,
de acuerdo con el siguiente diccionario:
# Diccionario código: país.
paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}
Si el código ingresado no se encuentra en
el diccionario, debe imprimir un mensaje en
pantalla y volver a preguntar. Si el usuario
escribe “salir”, el programa debe terminar.
"""
paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

#"utlizamos un while para cada situacion que se presente"
while True:
    cod = input ("Ingrese codigo: ")
    try:
        print("El codigo de pais es:", paises[cod])
    #dentificamos el tipo de error que puede haber
    except KeyError:
        if cod == "salir":
            print("Gracias por utilzar el programa")
            break
        else:
            print("Codigo no encontrado, por favor intente de nuevo")
            