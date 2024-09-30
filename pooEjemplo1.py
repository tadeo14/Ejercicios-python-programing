


class Fabrica():
    #creamos el metodo init
    def __init__(self):
        #definimos atributos
        self.color = "amarillo"
        self.tipo = "futbol"
        self.material = "cuero"
    
    #definimos un metodo
    def picar(self):
        print("El balon esta picado")

#La palabra self se usa para guardar el espacio del nombre del objeto que corresponde

#########################################

obj1 = Fabrica()

#instancia 
obj2= Fabrica()


print(obj1.color)

obj2.color = "Naranja"
print(obj2.color)

#aplicamos el metodo
obj1.picar()