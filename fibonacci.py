

def fibo(t):
    """
    Creamos primero la lista
    mientras el termino de len sea menor al termino
    haremos la suma del utlimo y anteultimo de f
    luego agregamos al final la suma 
    """
    f = [0,1]
    while len (f) < t:
        suma = f[-1] + f[-2]
        f.append(suma)
    print(f)


############################

fibo(20)