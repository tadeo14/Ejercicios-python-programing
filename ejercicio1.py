""" 
Crear un bucle que almacene la suma de todos los elementos 
de la lista menos el ultimo

Hay tres soluciones posibles. 
1_ Utilizando del. Lo que hara es elimninar el utlimo elemento de la lista.
2_ Utilizando 
    for n in lista[:-1]:
3_ lista = [10,20,30,40]

aux = 0 

componente = 0

for n in lista: 
    aux = aux + n
    componente = componente + 1
    if componente == len(lista) -1:
    break

print(aux)


"""

lista = [10,20,30,40]

aux = 0 

"eliminamos el ultimo elemento"
del lista  [-1]

for n in lista: 
    aux = aux + n


print(aux)