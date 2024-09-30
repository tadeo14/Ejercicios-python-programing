


class Fabrica():
    
    def __init__(self,c,t,m):
        #correr al inicio cuando se crea la instancia
        #definimos atributos
        self.color = c
        self.tipo = t
        self.material = m
    
    #definimos un metodo
    def picar(self):
        if self.tipo.lower() == "futbol" :
            print("El balon esta picado")
        elif self.tipo.lower() == "playa" :
            for n in range (3):
                print("El balon esta picado")
        else: 
            print("pum")
#La palabra self se usa para guardar el espacio del nombre del objeto que corresponde

#########################################

obj1 = Fabrica("Turquesa","playa","Plastico") #Pasamos los atributos como parametros

print(obj1.color)
print(obj1.tipo)
print(obj1.material)

obj1.tipo = "futbol"

obj1.picar()