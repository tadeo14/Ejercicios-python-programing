""" 
Crear un bucle que almacene la suma de todos los elementos 
de la lista menos el ultimo
"""

lista = [10,20,30,40]

aux = 0 

"eliminamos el ultimo elemento"
del lista  [-1]

for n in lista: 
    aux = aux + n


print(aux)